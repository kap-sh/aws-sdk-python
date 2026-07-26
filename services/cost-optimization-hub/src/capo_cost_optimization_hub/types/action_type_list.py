"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ActionTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.action_type

ActionTypeList: TypeAlias = list[
    "capo_cost_optimization_hub.types.action_type.ActionType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionTypeList) -> list:
    import capo_cost_optimization_hub.types.action_type

    out: list = []
    for item in value:
        out.append(
            capo_cost_optimization_hub.types.action_type.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ActionTypeList:
    import capo_cost_optimization_hub.types.action_type

    out: ActionTypeList = []
    for item in data:
        out.append(
            capo_cost_optimization_hub.types.action_type.deserialize_aws_json_1_0(item)
        )
    return out
