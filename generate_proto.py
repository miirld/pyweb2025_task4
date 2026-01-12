import subprocess
import sys

subprocess.run([
    sys.executable, "-m", "grpc_tools.protoc",
    "-Iprotobufs",
    "--python_out=app/generated",
    "--grpc_python_out=app/generated",
    "protobufs/glossary.proto"
])

grpc_file = "app/generated/glossary_pb2_grpc.py"

with open(grpc_file, 'r') as f:
    content = f.read()

content = content.replace(
    'import glossary_pb2 as glossary__pb2',
    'from . import glossary_pb2 as glossary__pb2'
)

with open(grpc_file, 'w') as f:
    f.write(content)
