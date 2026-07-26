"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileSystemOpenZFSOption``."""

from typing import Literal, TypeAlias, cast

DeleteFileSystemOpenZFSOption: TypeAlias = Literal[
    "DELETE_CHILD_VOLUMES_AND_SNAPSHOTS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileSystemOpenZFSOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeleteFileSystemOpenZFSOption:
    return cast(DeleteFileSystemOpenZFSOption, data)
