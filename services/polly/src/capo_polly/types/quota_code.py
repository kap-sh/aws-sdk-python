"""Generated from Smithy shape ``com.amazonaws.polly#QuotaCode``."""

from typing import Literal, TypeAlias, cast

QuotaCode: TypeAlias = Literal[
    "input-stream-inbound-event-timeout",
    "input-stream-timeout",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaCode) -> str:
    return value


def deserialize_json(data: str) -> QuotaCode:
    return cast(QuotaCode, data)
