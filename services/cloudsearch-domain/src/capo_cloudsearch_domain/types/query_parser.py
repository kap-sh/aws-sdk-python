"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#QueryParser``."""

from typing import Literal, TypeAlias, cast

QueryParser: TypeAlias = Literal[
    "simple",
    "structured",
    "lucene",
    "dismax",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryParser) -> str:
    return value


def deserialize_json(data: str) -> QueryParser:
    return cast(QueryParser, data)
