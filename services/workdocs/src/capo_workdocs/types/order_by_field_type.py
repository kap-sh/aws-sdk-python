"""Generated from Smithy shape ``com.amazonaws.workdocs#OrderByFieldType``."""

from typing import Literal, TypeAlias, cast

OrderByFieldType: TypeAlias = Literal[
    "RELEVANCE",
    "NAME",
    "SIZE",
    "CREATED_TIMESTAMP",
    "MODIFIED_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrderByFieldType) -> str:
    return value


def deserialize_json(data: str) -> OrderByFieldType:
    return cast(OrderByFieldType, data)
