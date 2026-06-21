"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#TtlDurationUnit``."""

from typing import Literal, TypeAlias, cast

TtlDurationUnit: TypeAlias = Literal[
    "Seconds",
    "Minutes",
    "Hours",
    "Days",
    "Weeks",
]


# --- restJson1 ser/de ---
def serialize_json(value: TtlDurationUnit) -> str:
    return value


def deserialize_json(data: str) -> TtlDurationUnit:
    return cast(TtlDurationUnit, data)
