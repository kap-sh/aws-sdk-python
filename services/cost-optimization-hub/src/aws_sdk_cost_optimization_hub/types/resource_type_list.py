"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.resource_type

ResourceTypeList: TypeAlias = list[
    "aws_sdk_cost_optimization_hub.types.resource_type.ResourceType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTypeList) -> list:
    import aws_sdk_cost_optimization_hub.types.resource_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_optimization_hub.types.resource_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceTypeList:
    import aws_sdk_cost_optimization_hub.types.resource_type

    out: ResourceTypeList = []
    for item in data:
        out.append(
            aws_sdk_cost_optimization_hub.types.resource_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
