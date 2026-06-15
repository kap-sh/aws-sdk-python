"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#QueryParser``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudsearch_domain.errors import DeserializationError

QueryParser: TypeAlias = Literal[
    "simple",
    "structured",
    "lucene",
    "dismax",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "simple",
        "structured",
        "lucene",
        "dismax",
    )
)


def serialize_json(value: QueryParser) -> str:
    return value


def deserialize_json(data: str) -> QueryParser:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryParser value: {data!r}")
    return cast(QueryParser, data)
