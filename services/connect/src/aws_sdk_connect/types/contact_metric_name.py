"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricName``."""

from typing import Literal, TypeAlias, cast

ContactMetricName: TypeAlias = Literal[
    "ESTIMATED_WAIT_TIME",
    "POSITION_IN_QUEUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricName) -> str:
    return value


def deserialize_json(data: str) -> ContactMetricName:
    return cast(ContactMetricName, data)
