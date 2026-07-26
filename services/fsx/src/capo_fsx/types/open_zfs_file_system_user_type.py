"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSFileSystemUserType``."""

from typing import Literal, TypeAlias, cast

OpenZFSFileSystemUserType: TypeAlias = Literal["POSIX",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSFileSystemUserType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSFileSystemUserType:
    return cast(OpenZFSFileSystemUserType, data)
