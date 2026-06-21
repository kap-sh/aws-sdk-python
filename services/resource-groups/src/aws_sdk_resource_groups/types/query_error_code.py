"""Generated from Smithy shape ``com.amazonaws.resourcegroups#QueryErrorCode``."""

from typing import Literal, TypeAlias, cast

QueryErrorCode: TypeAlias = Literal[
    "CLOUDFORMATION_STACK_INACTIVE",
    "CLOUDFORMATION_STACK_NOT_EXISTING",
    "CLOUDFORMATION_STACK_UNASSUMABLE_ROLE",
    "RESOURCE_TYPE_NOT_SUPPORTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueryErrorCode) -> str:
    return value


def deserialize_json(data: str) -> QueryErrorCode:
    return cast(QueryErrorCode, data)
