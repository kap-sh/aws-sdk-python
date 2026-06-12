"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.resource_arn

ResourceArnList: TypeAlias = list[
    "aws_sdk_resource_groups.types.resource_arn.ResourceArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArnList:
    return list(data)
