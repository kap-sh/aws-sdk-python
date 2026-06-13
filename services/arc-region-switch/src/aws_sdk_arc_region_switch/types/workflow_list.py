"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#WorkflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.workflow

WorkflowList: TypeAlias = list["aws_sdk_arc_region_switch.types.workflow.Workflow"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowList) -> list:
    import aws_sdk_arc_region_switch.types.workflow

    out: list = []
    for item in value:
        out.append(
            aws_sdk_arc_region_switch.types.workflow.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WorkflowList:
    import aws_sdk_arc_region_switch.types.workflow

    out: WorkflowList = []
    for item in data:
        out.append(
            aws_sdk_arc_region_switch.types.workflow.deserialize_aws_json_1_0(item)
        )
    return out
