"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ExplainMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

ExplainMode: TypeAlias = Literal[
    "STATIC",
    "DETAILS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATIC",
        "DETAILS",
    )
)


def serialize_json(value: ExplainMode) -> str:
    return value


def deserialize_json(data: str) -> ExplainMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExplainMode value: {data!r}")
    return cast(ExplainMode, data)
