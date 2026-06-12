"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AggregateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

AggregateType: TypeAlias = Literal[
    "AVERAGE",
    "COUNT",
    "MAXIMUM",
    "MINIMUM",
    "SUM",
    "STANDARD_DEVIATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVERAGE",
        "COUNT",
        "MAXIMUM",
        "MINIMUM",
        "SUM",
        "STANDARD_DEVIATION",
    )
)


def serialize_json(value: AggregateType) -> str:
    return value


def deserialize_json(data: str) -> AggregateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggregateType value: {data!r}")
    return cast(AggregateType, data)
