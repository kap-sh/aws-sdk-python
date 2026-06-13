"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ImplementationEffortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.implementation_effort

ImplementationEffortList: TypeAlias = list[
    "aws_sdk_cost_optimization_hub.types.implementation_effort.ImplementationEffort"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImplementationEffortList) -> list:
    import aws_sdk_cost_optimization_hub.types.implementation_effort

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_optimization_hub.types.implementation_effort.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ImplementationEffortList:
    import aws_sdk_cost_optimization_hub.types.implementation_effort

    out: ImplementationEffortList = []
    for item in data:
        out.append(
            aws_sdk_cost_optimization_hub.types.implementation_effort.deserialize_aws_json_1_0(
                item
            )
        )
    return out
