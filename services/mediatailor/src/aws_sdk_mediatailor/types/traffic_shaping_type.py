"""Generated from Smithy shape ``com.amazonaws.mediatailor#TrafficShapingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

TrafficShapingType: TypeAlias = Literal[
    "RETRIEVAL_WINDOW",
    "TPS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RETRIEVAL_WINDOW",
        "TPS",
    )
)


def serialize_json(value: TrafficShapingType) -> str:
    return value


def deserialize_json(data: str) -> TrafficShapingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrafficShapingType value: {data!r}")
    return cast(TrafficShapingType, data)
