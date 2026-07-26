"""Generated from Smithy shape ``com.amazonaws.appsync#GraphQLApiVisibility``."""

from typing import Literal, TypeAlias, cast

GraphQLApiVisibility: TypeAlias = Literal[
    "GLOBAL",
    "PRIVATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphQLApiVisibility) -> str:
    return value


def deserialize_json(data: str) -> GraphQLApiVisibility:
    return cast(GraphQLApiVisibility, data)
