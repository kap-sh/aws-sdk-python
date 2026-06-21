"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemLifecycle``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle status of the file system.</p>"""
FileSystemLifecycle: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "FAILED",
    "DELETING",
    "MISCONFIGURED",
    "UPDATING",
    "MISCONFIGURED_UNAVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemLifecycle:
    return cast(FileSystemLifecycle, data)
