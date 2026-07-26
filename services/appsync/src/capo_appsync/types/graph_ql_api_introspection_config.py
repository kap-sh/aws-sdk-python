"""Generated from Smithy shape ``com.amazonaws.appsync#GraphQLApiIntrospectionConfig``."""

from typing import Literal, TypeAlias, cast

GraphQLApiIntrospectionConfig: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GraphQLApiIntrospectionConfig) -> str:
    return value


def deserialize_json(data: str) -> GraphQLApiIntrospectionConfig:
    return cast(GraphQLApiIntrospectionConfig, data)
