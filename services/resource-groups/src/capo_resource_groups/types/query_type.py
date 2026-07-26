"""Generated from Smithy shape ``com.amazonaws.resourcegroups#QueryType``."""

from typing import Literal, TypeAlias, cast

QueryType: TypeAlias = Literal[
    "TAG_FILTERS_1_0",
    "CLOUDFORMATION_STACK_1_0",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryType) -> str:
    return value


def deserialize_json(data: str) -> QueryType:
    return cast(QueryType, data)
