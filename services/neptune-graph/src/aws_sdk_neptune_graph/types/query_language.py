"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QueryLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune_graph.errors import DeserializationError

QueryLanguage: TypeAlias = Literal["OPEN_CYPHER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OPEN_CYPHER",))


def serialize_json(value: QueryLanguage) -> str:
    return value


def deserialize_json(data: str) -> QueryLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryLanguage value: {data!r}")
    return cast(QueryLanguage, data)
