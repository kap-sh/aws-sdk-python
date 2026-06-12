"""Generated from Smithy shape ``com.amazonaws.resourcegroups#QueryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

QueryType: TypeAlias = Literal[
    "TAG_FILTERS_1_0",
    "CLOUDFORMATION_STACK_1_0",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TAG_FILTERS_1_0",
        "CLOUDFORMATION_STACK_1_0",
    )
)


def serialize_json(value: QueryType) -> str:
    return value


def deserialize_json(data: str) -> QueryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryType value: {data!r}")
    return cast(QueryType, data)
