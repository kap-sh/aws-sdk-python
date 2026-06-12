"""Generated from Smithy shape ``com.amazonaws.appstream#StackErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

StackErrorCode: TypeAlias = Literal[
    "STORAGE_CONNECTOR_ERROR",
    "INTERNAL_SERVICE_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STORAGE_CONNECTOR_ERROR",
        "INTERNAL_SERVICE_ERROR",
    )
)


def serialize_aws_json_1_1(value: StackErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StackErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StackErrorCode value: {data!r}")
    return cast(StackErrorCode, data)
