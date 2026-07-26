"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeliveryStatus``."""

from typing import Literal, TypeAlias, cast

DeliveryStatus: TypeAlias = Literal[
    "SUCCESSFUL",
    "THROTTLED",
    "TEMPORARY_FAILURE",
    "PERMANENT_FAILURE",
    "UNKNOWN_FAILURE",
    "OPT_OUT",
    "DUPLICATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeliveryStatus) -> str:
    return value


def deserialize_json(data: str) -> DeliveryStatus:
    return cast(DeliveryStatus, data)
