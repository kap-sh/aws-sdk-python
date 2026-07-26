"""Generated from Smithy shape ``com.amazonaws.costexplorer#ResourceTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.resource_tag_key

ResourceTagKeyList: TypeAlias = list[
    "capo_cost_explorer.types.resource_tag_key.ResourceTagKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTagKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceTagKeyList:
    return list(data)
