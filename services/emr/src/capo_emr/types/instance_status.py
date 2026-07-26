"""Generated from Smithy shape ``com.amazonaws.emr#InstanceStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.instance_state
    import capo_emr.types.instance_state_change_reason
    import capo_emr.types.instance_timeline


class InstanceStatus(TypedDict, closed=True):
    state: NotRequired["capo_emr.types.instance_state.InstanceState"]
    """<p>The current state of the instance.</p>"""
    state_change_reason: NotRequired[
        "capo_emr.types.instance_state_change_reason.InstanceStateChangeReason"
    ]
    """<p>The details of the status change reason for the instance.</p>"""
    timeline: NotRequired["capo_emr.types.instance_timeline.InstanceTimeline"]
    """<p>The timeline of the instance status over time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_emr.types.instance_state

        out["State"] = capo_emr.types.instance_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        import capo_emr.types.instance_state_change_reason

        out["StateChangeReason"] = (
            capo_emr.types.instance_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "timeline" in value:
        import capo_emr.types.instance_timeline

        out["Timeline"] = capo_emr.types.instance_timeline.serialize_aws_json_1_1(
            value["timeline"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceStatus:
    out: InstanceStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_emr.types.instance_state

        out["state"] = capo_emr.types.instance_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        import capo_emr.types.instance_state_change_reason

        out["state_change_reason"] = (
            capo_emr.types.instance_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if "Timeline" in data:
        import capo_emr.types.instance_timeline

        out["timeline"] = capo_emr.types.instance_timeline.deserialize_aws_json_1_1(
            data["Timeline"]
        )
    return out
