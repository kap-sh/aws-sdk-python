"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#MinimalWorkflow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.execution_action


class MinimalWorkflow(TypedDict, closed=True):
    action: NotRequired[
        "aws_sdk_arc_region_switch.types.execution_action.ExecutionAction"
    ]
    """<p>The action for a minimal workflow, which can be Activate or Deactivate.</p>"""
    name: NotRequired["str"]
    """<p>The name for a minimal workflow</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MinimalWorkflow) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_arc_region_switch.types.execution_action

        out["action"] = (
            aws_sdk_arc_region_switch.types.execution_action.serialize_aws_json_1_0(
                value["action"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MinimalWorkflow:
    out: MinimalWorkflow = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_arc_region_switch.types.execution_action

        out["action"] = (
            aws_sdk_arc_region_switch.types.execution_action.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    return out
