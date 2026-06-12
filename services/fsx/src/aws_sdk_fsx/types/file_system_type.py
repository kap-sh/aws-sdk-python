"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

"""<p>The type of Amazon FSx file system.</p>"""
FileSystemType: TypeAlias = Literal[
    "WINDOWS",
    "LUSTRE",
    "ONTAP",
    "OPENZFS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS",
        "LUSTRE",
        "ONTAP",
        "OPENZFS",
    )
)


def serialize_aws_json_1_1(value: FileSystemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileSystemType value: {data!r}")
    return cast(FileSystemType, data)
