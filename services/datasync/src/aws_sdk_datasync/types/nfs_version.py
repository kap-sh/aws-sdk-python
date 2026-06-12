"""Generated from Smithy shape ``com.amazonaws.datasync#NfsVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

NfsVersion: TypeAlias = Literal[
    "AUTOMATIC",
    "NFS3",
    "NFS4_0",
    "NFS4_1",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "NFS3",
        "NFS4_0",
        "NFS4_1",
    )
)


def serialize_aws_json_1_1(value: NfsVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NfsVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NfsVersion value: {data!r}")
    return cast(NfsVersion, data)
