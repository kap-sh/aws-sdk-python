"""Generated from Smithy shape ``com.amazonaws.iot#CustomMetricType``."""

from typing import Literal, TypeAlias, cast

CustomMetricType: TypeAlias = Literal[
    "string-list",
    "ip-address-list",
    "number-list",
    "number",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetricType) -> str:
    return value


def deserialize_json(data: str) -> CustomMetricType:
    return cast(CustomMetricType, data)
