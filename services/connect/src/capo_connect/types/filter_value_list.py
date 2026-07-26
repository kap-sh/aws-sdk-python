"""Generated from Smithy shape ``com.amazonaws.connect#FilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.resource_arn_or_id

FilterValueList: TypeAlias = list[
    "capo_connect.types.resource_arn_or_id.ResourceArnOrId"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterValueList:
    return list(data)
