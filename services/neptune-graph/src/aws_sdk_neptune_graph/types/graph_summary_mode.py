"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GraphSummaryMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

GraphSummaryMode: TypeAlias = Literal[
    "BASIC",
    "DETAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "DETAILED",
    )
)


def serialize_json(value: GraphSummaryMode) -> str:
    return value


def deserialize_json(data: str) -> GraphSummaryMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GraphSummaryMode value: {data!r}")
    return cast(GraphSummaryMode, data)
