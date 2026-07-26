"""Generated from Smithy shape ``com.amazonaws.connect#FailureReasonCode``."""

from typing import Literal, TypeAlias, cast

FailureReasonCode: TypeAlias = Literal[
    "INVALID_ATTRIBUTE_KEY",
    "INVALID_CUSTOMER_ENDPOINT",
    "INVALID_SYSTEM_ENDPOINT",
    "INVALID_QUEUE",
    "INVALID_OUTBOUND_STRATEGY",
    "MISSING_CAMPAIGN",
    "MISSING_CUSTOMER_ENDPOINT",
    "MISSING_QUEUE_ID_AND_SYSTEM_ENDPOINT",
    "REQUEST_THROTTLED",
    "IDEMPOTENCY_EXCEPTION",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: FailureReasonCode) -> str:
    return value


def deserialize_json(data: str) -> FailureReasonCode:
    return cast(FailureReasonCode, data)
