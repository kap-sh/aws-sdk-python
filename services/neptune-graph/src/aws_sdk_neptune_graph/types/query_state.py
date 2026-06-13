"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QueryState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

QueryState: TypeAlias = Literal[
    "RUNNING",
    "WAITING",
    "CANCELLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "WAITING",
        "CANCELLING",
    )
)


def serialize_json(value: QueryState) -> str:
    return value


def deserialize_json(data: str) -> QueryState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryState value: {data!r}")
    return cast(QueryState, data)
