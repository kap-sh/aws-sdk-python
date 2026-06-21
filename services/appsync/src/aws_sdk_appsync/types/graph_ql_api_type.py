"""Generated from Smithy shape ``com.amazonaws.appsync#GraphQLApiType``."""

from typing import Literal, TypeAlias, cast

GraphQLApiType: TypeAlias = Literal[
    "GRAPHQL",
    "MERGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphQLApiType) -> str:
    return value


def deserialize_json(data: str) -> GraphQLApiType:
    return cast(GraphQLApiType, data)
