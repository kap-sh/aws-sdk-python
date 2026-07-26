"""Generated from Smithy shape ``com.amazonaws.shield#ResourceArnFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.resource_arn

ResourceArnFilterList: TypeAlias = list["capo_shield.types.resource_arn.ResourceArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceArnFilterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceArnFilterList:
    return list(data)
