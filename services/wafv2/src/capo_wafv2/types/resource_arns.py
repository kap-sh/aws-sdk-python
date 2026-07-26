"""Generated from Smithy shape ``com.amazonaws.wafv2#ResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.resource_arn

ResourceArns: TypeAlias = list["capo_wafv2.types.resource_arn.ResourceArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceArns:
    return list(data)
