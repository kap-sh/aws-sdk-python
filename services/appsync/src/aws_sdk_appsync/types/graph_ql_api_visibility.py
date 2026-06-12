"""Generated from Smithy shape ``com.amazonaws.appsync#GraphQLApiVisibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

GraphQLApiVisibility: TypeAlias = Literal[
    "GLOBAL",
    "PRIVATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GLOBAL",
        "PRIVATE",
    )
)


def serialize_json(value: GraphQLApiVisibility) -> str:
    return value


def deserialize_json(data: str) -> GraphQLApiVisibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GraphQLApiVisibility value: {data!r}")
    return cast(GraphQLApiVisibility, data)
