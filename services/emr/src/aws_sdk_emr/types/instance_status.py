"""Generated from Smithy shape ``com.amazonaws.emr#InstanceStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_state
    import aws_sdk_emr.types.instance_state_change_reason
    import aws_sdk_emr.types.instance_timeline


class InstanceStatus(TypedDict):
    state: NotRequired["aws_sdk_emr.types.instance_state.InstanceState"]
    """<p>The current state of the instance.</p>"""
    state_change_reason: NotRequired[
        "aws_sdk_emr.types.instance_state_change_reason.InstanceStateChangeReason"
    ]
    """<p>The details of the status change reason for the instance.</p>"""
    timeline: NotRequired["aws_sdk_emr.types.instance_timeline.InstanceTimeline"]
    """<p>The timeline of the instance status over time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_emr.types.instance_state

        out["State"] = aws_sdk_emr.types.instance_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        import aws_sdk_emr.types.instance_state_change_reason

        out["StateChangeReason"] = (
            aws_sdk_emr.types.instance_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "timeline" in value:
        import aws_sdk_emr.types.instance_timeline

        out["Timeline"] = aws_sdk_emr.types.instance_timeline.serialize_aws_json_1_1(
            value["timeline"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceStatus:
    out: InstanceStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_emr.types.instance_state

        out["state"] = aws_sdk_emr.types.instance_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        import aws_sdk_emr.types.instance_state_change_reason

        out["state_change_reason"] = (
            aws_sdk_emr.types.instance_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if "Timeline" in data:
        import aws_sdk_emr.types.instance_timeline

        out["timeline"] = aws_sdk_emr.types.instance_timeline.deserialize_aws_json_1_1(
            data["Timeline"]
        )
    return out
