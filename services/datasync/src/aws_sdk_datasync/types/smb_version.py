"""Generated from Smithy shape ``com.amazonaws.datasync#SmbVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

SmbVersion: TypeAlias = Literal[
    "AUTOMATIC",
    "SMB2",
    "SMB3",
    "SMB1",
    "SMB2_0",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "SMB2",
        "SMB3",
        "SMB1",
        "SMB2_0",
    )
)


def serialize_aws_json_1_1(value: SmbVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SmbVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SmbVersion value: {data!r}")
    return cast(SmbVersion, data)
