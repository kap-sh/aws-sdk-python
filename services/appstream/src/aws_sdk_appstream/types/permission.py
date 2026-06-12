"""Generated from Smithy shape ``com.amazonaws.appstream#Permission``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

Permission: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: Permission) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Permission:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Permission value: {data!r}")
    return cast(Permission, data)
