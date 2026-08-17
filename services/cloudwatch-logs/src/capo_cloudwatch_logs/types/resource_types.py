"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResourceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.resource_type

ResourceTypes: TypeAlias = list["capo_cloudwatch_logs.types.resource_type.ResourceType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceTypes:
    return [item for item in data if item is not None]
