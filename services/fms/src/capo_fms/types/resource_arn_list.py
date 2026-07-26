"""Generated from Smithy shape ``com.amazonaws.fms#ResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.resource_arn

ResourceArnList: TypeAlias = list["capo_fms.types.resource_arn.ResourceArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceArnList:
    return list(data)
