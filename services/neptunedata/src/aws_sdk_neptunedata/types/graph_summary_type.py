"""Generated from Smithy shape ``com.amazonaws.neptunedata#GraphSummaryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

GraphSummaryType: TypeAlias = Literal[
    "basic",
    "detailed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "basic",
        "detailed",
    )
)


def serialize_json(value: GraphSummaryType) -> str:
    return value


def deserialize_json(data: str) -> GraphSummaryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GraphSummaryType value: {data!r}")
    return cast(GraphSummaryType, data)
