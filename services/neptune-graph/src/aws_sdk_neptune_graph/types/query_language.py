"""Generated from Smithy shape ``com.amazonaws.neptunegraph#QueryLanguage``."""

from typing import Literal, TypeAlias, cast

QueryLanguage: TypeAlias = Literal["OPEN_CYPHER",]


# --- restJson1 ser/de ---
def serialize_json(value: QueryLanguage) -> str:
    return value


def deserialize_json(data: str) -> QueryLanguage:
    return cast(QueryLanguage, data)
