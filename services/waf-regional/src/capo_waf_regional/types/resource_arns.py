"""Generated from Smithy shape ``com.amazonaws.wafregional#ResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_arn

ResourceArns: TypeAlias = list["capo_waf_regional.types.resource_arn.ResourceArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceArns:
    return list(data)
