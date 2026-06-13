"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#PlanWarnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.resource_warning

PlanWarnings: TypeAlias = list[
    "aws_sdk_arc_region_switch.types.resource_warning.ResourceWarning"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PlanWarnings) -> list:
    import aws_sdk_arc_region_switch.types.resource_warning

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_region_switch.types.resource_warning.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PlanWarnings:
    import aws_sdk_arc_region_switch.types.resource_warning

    out: PlanWarnings = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.resource_warning.deserialize_aws_json_1_0(
                item
            )
        )
    return out
