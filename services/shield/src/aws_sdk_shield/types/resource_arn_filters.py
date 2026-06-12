"""Generated from Smithy shape ``com.amazonaws.shield#ResourceArnFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.resource_arn

ResourceArnFilters: TypeAlias = list["aws_sdk_shield.types.resource_arn.ResourceArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceArnFilters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceArnFilters:
    return list(data)
