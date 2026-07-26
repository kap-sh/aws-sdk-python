"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of Amazon FSx file system.</p>"""
FileSystemType: TypeAlias = Literal[
    "WINDOWS",
    "LUSTRE",
    "ONTAP",
    "OPENZFS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemType:
    return cast(FileSystemType, data)
