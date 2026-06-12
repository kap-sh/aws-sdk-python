"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#ErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events_data.errors import DeserializationError

ErrorCode: TypeAlias = Literal[
    "ResourceNotFoundException",
    "InvalidRequestException",
    "InternalFailureException",
    "ServiceUnavailableException",
    "ThrottlingException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceNotFoundException",
        "InvalidRequestException",
        "InternalFailureException",
        "ServiceUnavailableException",
        "ThrottlingException",
    )
)


def serialize_json(value: ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ErrorCode value: {data!r}")
    return cast(ErrorCode, data)
