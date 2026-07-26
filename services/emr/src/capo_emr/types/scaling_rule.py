"""Generated from Smithy shape ``com.amazonaws.emr#ScalingRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.scaling_action
    import capo_emr.types.scaling_trigger
    import capo_emr.types.string


class ScalingRule(TypedDict, closed=True):
    name: NotRequired["capo_emr.types.string.String"]
    """<p>The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.</p>"""
    description: NotRequired["capo_emr.types.string.String"]
    """<p>A friendly, more verbose description of the automatic scaling rule.</p>"""
    action: NotRequired["capo_emr.types.scaling_action.ScalingAction"]
    """<p>The conditions that trigger an automatic scaling activity.</p>"""
    trigger: NotRequired["capo_emr.types.scaling_trigger.ScalingTrigger"]
    """<p>The CloudWatch alarm definition that determines when automatic scaling activity is triggered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingRule) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "action" in value:
        import capo_emr.types.scaling_action

        out["Action"] = capo_emr.types.scaling_action.serialize_aws_json_1_1(
            value["action"]
        )
    if "trigger" in value:
        import capo_emr.types.scaling_trigger

        out["Trigger"] = capo_emr.types.scaling_trigger.serialize_aws_json_1_1(
            value["trigger"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingRule:
    out: ScalingRule = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Action" in data:
        import capo_emr.types.scaling_action

        out["action"] = capo_emr.types.scaling_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if "Trigger" in data:
        import capo_emr.types.scaling_trigger

        out["trigger"] = capo_emr.types.scaling_trigger.deserialize_aws_json_1_1(
            data["Trigger"]
        )
    return out
