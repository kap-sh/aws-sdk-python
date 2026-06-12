"""Generated from Smithy shape ``com.amazonaws.emr#InstanceGroupStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_group_state
    import aws_sdk_emr.types.instance_group_state_change_reason
    import aws_sdk_emr.types.instance_group_timeline


class InstanceGroupStatus(TypedDict):
    state: NotRequired["aws_sdk_emr.types.instance_group_state.InstanceGroupState"]
    """<p>The current state of the instance group.</p>"""
    state_change_reason: NotRequired[
        "aws_sdk_emr.types.instance_group_state_change_reason.InstanceGroupStateChangeReason"
    ]
    """<p>The status change reason details for the instance group.</p>"""
    timeline: NotRequired[
        "aws_sdk_emr.types.instance_group_timeline.InstanceGroupTimeline"
    ]
    """<p>The timeline of the instance group status over time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_emr.types.instance_group_state

        out["State"] = aws_sdk_emr.types.instance_group_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        import aws_sdk_emr.types.instance_group_state_change_reason

        out["StateChangeReason"] = (
            aws_sdk_emr.types.instance_group_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "timeline" in value:
        import aws_sdk_emr.types.instance_group_timeline

        out["Timeline"] = (
            aws_sdk_emr.types.instance_group_timeline.serialize_aws_json_1_1(
                value["timeline"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupStatus:
    out: InstanceGroupStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_emr.types.instance_group_state

        out["state"] = aws_sdk_emr.types.instance_group_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        import aws_sdk_emr.types.instance_group_state_change_reason

        out["state_change_reason"] = (
            aws_sdk_emr.types.instance_group_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if "Timeline" in data:
        import aws_sdk_emr.types.instance_group_timeline

        out["timeline"] = (
            aws_sdk_emr.types.instance_group_timeline.deserialize_aws_json_1_1(
                data["Timeline"]
            )
        )
    return out
