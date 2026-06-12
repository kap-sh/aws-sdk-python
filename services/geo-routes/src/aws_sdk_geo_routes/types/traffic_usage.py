"""Generated from Smithy shape ``com.amazonaws.georoutes#TrafficUsage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

TrafficUsage: TypeAlias = Literal[
    "IgnoreTrafficData",
    "UseTrafficData",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IgnoreTrafficData",
        "UseTrafficData",
    )
)


def serialize_json(value: TrafficUsage) -> str:
    return value


def deserialize_json(data: str) -> TrafficUsage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrafficUsage value: {data!r}")
    return cast(TrafficUsage, data)
