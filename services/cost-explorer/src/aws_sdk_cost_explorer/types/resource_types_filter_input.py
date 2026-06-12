"""Generated from Smithy shape ``com.amazonaws.costexplorer#ResourceTypesFilterInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.resource_type

ResourceTypesFilterInput: TypeAlias = list[
    "aws_sdk_cost_explorer.types.resource_type.ResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTypesFilterInput) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceTypesFilterInput:
    return list(data)
