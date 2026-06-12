"""Generated from Smithy shape ``com.amazonaws.cloud9#Permissions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloud9.errors import DeserializationError

Permissions: TypeAlias = Literal[
    "owner",
    "read-write",
    "read-only",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "owner",
        "read-write",
        "read-only",
    )
)


def serialize_aws_json_1_1(value: Permissions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Permissions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Permissions value: {data!r}")
    return cast(Permissions, data)
