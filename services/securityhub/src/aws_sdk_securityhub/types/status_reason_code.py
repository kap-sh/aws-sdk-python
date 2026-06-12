"""Generated from Smithy shape ``com.amazonaws.securityhub#StatusReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

StatusReasonCode: TypeAlias = Literal[
    "NO_AVAILABLE_CONFIGURATION_RECORDER",
    "MAXIMUM_NUMBER_OF_CONFIG_RULES_EXCEEDED",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_AVAILABLE_CONFIGURATION_RECORDER",
        "MAXIMUM_NUMBER_OF_CONFIG_RULES_EXCEEDED",
        "INTERNAL_ERROR",
    )
)


def serialize_json(value: StatusReasonCode) -> str:
    return value


def deserialize_json(data: str) -> StatusReasonCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusReasonCode value: {data!r}")
    return cast(StatusReasonCode, data)
