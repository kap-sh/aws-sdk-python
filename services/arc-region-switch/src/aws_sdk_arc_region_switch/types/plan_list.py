"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#PlanList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.abbreviated_plan

PlanList: TypeAlias = list[
    "aws_sdk_arc_region_switch.types.abbreviated_plan.AbbreviatedPlan"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PlanList) -> list:
    import aws_sdk_arc_region_switch.types.abbreviated_plan

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_region_switch.types.abbreviated_plan.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PlanList:
    import aws_sdk_arc_region_switch.types.abbreviated_plan

    out: PlanList = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.abbreviated_plan.deserialize_aws_json_1_0(
                item
            )
        )
    return out
