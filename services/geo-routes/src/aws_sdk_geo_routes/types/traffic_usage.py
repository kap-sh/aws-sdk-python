"""Generated from Smithy shape ``com.amazonaws.georoutes#TrafficUsage``."""

from typing import Literal, TypeAlias, cast

TrafficUsage: TypeAlias = Literal[
    "IgnoreTrafficData",
    "UseTrafficData",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficUsage) -> str:
    return value


def deserialize_json(data: str) -> TrafficUsage:
    return cast(TrafficUsage, data)
