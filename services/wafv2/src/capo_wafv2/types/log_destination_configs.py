"""Generated from Smithy shape ``com.amazonaws.wafv2#LogDestinationConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.resource_arn

LogDestinationConfigs: TypeAlias = list["capo_wafv2.types.resource_arn.ResourceArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogDestinationConfigs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogDestinationConfigs:
    return list(data)
