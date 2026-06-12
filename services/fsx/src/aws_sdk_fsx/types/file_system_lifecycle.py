"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "CREATING",
        "FAILED",
        "DELETING",
        "MISCONFIGURED",
        "UPDATING",
        "MISCONFIGURED_UNAVAILABLE",
    )
)


def serialize_aws_json_1_1(value: FileSystemLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileSystemLifecycle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileSystemLifecycle value: {data!r}")
    return cast(FileSystemLifecycle, data)
