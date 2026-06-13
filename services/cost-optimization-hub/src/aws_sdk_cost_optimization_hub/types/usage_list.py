"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#UsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.usage

UsageList: TypeAlias = list["aws_sdk_cost_optimization_hub.types.usage.Usage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UsageList) -> list:
    import aws_sdk_cost_optimization_hub.types.usage

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_optimization_hub.types.usage.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UsageList:
    import aws_sdk_cost_optimization_hub.types.usage

    out: UsageList = []
    for item in data:
        out.append(
            aws_sdk_cost_optimization_hub.types.usage.deserialize_aws_json_1_0(item)
        )
    return out
