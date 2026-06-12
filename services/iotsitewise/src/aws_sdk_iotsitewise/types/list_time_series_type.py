"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListTimeSeriesType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ListTimeSeriesType: TypeAlias = Literal[
    "ASSOCIATED",
    "DISASSOCIATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATED",
        "DISASSOCIATED",
    )
)


def serialize_json(value: ListTimeSeriesType) -> str:
    return value


def deserialize_json(data: str) -> ListTimeSeriesType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListTimeSeriesType value: {data!r}")
    return cast(ListTimeSeriesType, data)
