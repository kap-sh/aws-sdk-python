"""Generated from Smithy shape ``com.amazonaws.securityhub#StatusReasonCode``."""

from typing import Literal, TypeAlias, cast

StatusReasonCode: TypeAlias = Literal[
    "NO_AVAILABLE_CONFIGURATION_RECORDER",
    "MAXIMUM_NUMBER_OF_CONFIG_RULES_EXCEEDED",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusReasonCode) -> str:
    return value


def deserialize_json(data: str) -> StatusReasonCode:
    return cast(StatusReasonCode, data)
