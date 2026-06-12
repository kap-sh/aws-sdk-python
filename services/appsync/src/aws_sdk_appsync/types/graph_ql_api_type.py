"""Generated from Smithy shape ``com.amazonaws.appsync#GraphQLApiType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

GraphQLApiType: TypeAlias = Literal[
    "GRAPHQL",
    "MERGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GRAPHQL",
        "MERGED",
    )
)


def serialize_json(value: GraphQLApiType) -> str:
    return value


def deserialize_json(data: str) -> GraphQLApiType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GraphQLApiType value: {data!r}")
    return cast(GraphQLApiType, data)
