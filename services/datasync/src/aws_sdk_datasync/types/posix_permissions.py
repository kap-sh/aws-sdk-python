"""Generated from Smithy shape ``com.amazonaws.datasync#PosixPermissions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

PosixPermissions: TypeAlias = Literal[
    "NONE",
    "PRESERVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "PRESERVE",
    )
)


def serialize_aws_json_1_1(value: PosixPermissions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PosixPermissions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PosixPermissions value: {data!r}")
    return cast(PosixPermissions, data)
