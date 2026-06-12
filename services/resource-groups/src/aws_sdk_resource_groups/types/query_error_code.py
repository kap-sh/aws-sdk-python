"""Generated from Smithy shape ``com.amazonaws.resourcegroups#QueryErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resource_groups.errors import DeserializationError

QueryErrorCode: TypeAlias = Literal[
    "CLOUDFORMATION_STACK_INACTIVE",
    "CLOUDFORMATION_STACK_NOT_EXISTING",
    "CLOUDFORMATION_STACK_UNASSUMABLE_ROLE",
    "RESOURCE_TYPE_NOT_SUPPORTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUDFORMATION_STACK_INACTIVE",
        "CLOUDFORMATION_STACK_NOT_EXISTING",
        "CLOUDFORMATION_STACK_UNASSUMABLE_ROLE",
        "RESOURCE_TYPE_NOT_SUPPORTED",
    )
)


def serialize_json(value: QueryErrorCode) -> str:
    return value


def deserialize_json(data: str) -> QueryErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryErrorCode value: {data!r}")
    return cast(QueryErrorCode, data)
