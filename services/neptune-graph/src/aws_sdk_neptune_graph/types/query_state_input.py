"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QueryStateInput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

QueryStateInput: TypeAlias = Literal[
    "ALL",
    "RUNNING",
    "WAITING",
    "CANCELLING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "RUNNING",
        "WAITING",
        "CANCELLING",
    )
)


def serialize_json(value: QueryStateInput) -> str:
    return value


def deserialize_json(data: str) -> QueryStateInput:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryStateInput value: {data!r}")
    return cast(QueryStateInput, data)
