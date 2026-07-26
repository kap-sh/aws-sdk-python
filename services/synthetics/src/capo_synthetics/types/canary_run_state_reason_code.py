"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunStateReasonCode``."""

from typing import Literal, TypeAlias, cast

CanaryRunStateReasonCode: TypeAlias = Literal[
    "CANARY_FAILURE",
    "EXECUTION_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRunStateReasonCode) -> str:
    return value


def deserialize_json(data: str) -> CanaryRunStateReasonCode:
    return cast(CanaryRunStateReasonCode, data)
