"""Generated from Smithy shape ``com.amazonaws.inspector#FailedItemErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

FailedItemErrorCode: TypeAlias = Literal[
    "INVALID_ARN",
    "DUPLICATE_ARN",
    "ITEM_DOES_NOT_EXIST",
    "ACCESS_DENIED",
    "LIMIT_EXCEEDED",
    "INTERNAL_ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_ARN",
        "DUPLICATE_ARN",
        "ITEM_DOES_NOT_EXIST",
        "ACCESS_DENIED",
        "LIMIT_EXCEEDED",
        "INTERNAL_ERROR",
    )
)


def serialize_aws_json_1_1(value: FailedItemErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailedItemErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FailedItemErrorCode value: {data!r}")
    return cast(FailedItemErrorCode, data)
