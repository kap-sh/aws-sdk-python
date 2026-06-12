"""Generated from Smithy shape ``com.amazonaws.appsync#GraphQLApiIntrospectionConfig``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

GraphQLApiIntrospectionConfig: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: GraphQLApiIntrospectionConfig) -> str:
    return value


def deserialize_json(data: str) -> GraphQLApiIntrospectionConfig:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GraphQLApiIntrospectionConfig value: {data!r}"
        )
    return cast(GraphQLApiIntrospectionConfig, data)
