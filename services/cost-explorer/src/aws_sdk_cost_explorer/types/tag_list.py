"""Generated from Smithy shape ``com.amazonaws.costexplorer#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.entity

TagList: TypeAlias = list["aws_sdk_cost_explorer.types.entity.Entity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagList:
    return list(data)
