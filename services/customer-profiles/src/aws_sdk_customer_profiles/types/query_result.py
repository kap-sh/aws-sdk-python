"""Generated from Smithy shape ``com.amazonaws.customerprofiles#QueryResult``."""

from typing import Literal, TypeAlias, cast

QueryResult: TypeAlias = Literal[
    "PRESENT",
    "ABSENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryResult) -> str:
    return value


def deserialize_json(data: str) -> QueryResult:
    return cast(QueryResult, data)
