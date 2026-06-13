"""Generated from Smithy shape ``com.amazonaws.emr#InstanceFleetStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.instance_fleet_state
    import aws_sdk_emr.types.instance_fleet_state_change_reason
    import aws_sdk_emr.types.instance_fleet_timeline


class InstanceFleetStatus(TypedDict):
    state: NotRequired["aws_sdk_emr.types.instance_fleet_state.InstanceFleetState"]
    """<p>A code representing the instance fleet status.</p> <ul> <li> <p> <code>PROVISIONING</code>—The instance fleet is provisioning Amazon EC2 resources and is not yet ready to run jobs.</p> </li> <li> <p> <code>BOOTSTRAPPING</code>—Amazon EC2 instances and other resources have been provisioned and the bootstrap actions specified for the instances are underway.</p> </li> <li> <p> <code>RUNNING</code>—Amazon EC2 instances and other resources are running. They are either executing jobs or waiting to execute jobs.</p> </li> <li> <p> <code>RESIZING</code>—A resize operation is underway. Amazon EC2 instances are either being added or removed.</p> </li> <li> <p> <code>SUSPENDED</code>—A resize operation could not complete. Existing Amazon EC2 instances are running, but instances can't be added or removed.</p> </li> <li> <p> <code>TERMINATING</code>—The instance fleet is terminating Amazon EC2 instances.</p> </li> <li> <p> <code>TERMINATED</code>—The instance fleet is no longer active, and all Amazon EC2 instances have been terminated.</p> </li> </ul>"""
    state_change_reason: NotRequired[
        "aws_sdk_emr.types.instance_fleet_state_change_reason.InstanceFleetStateChangeReason"
    ]
    """<p>Provides status change reason details for the instance fleet.</p>"""
    timeline: NotRequired[
        "aws_sdk_emr.types.instance_fleet_timeline.InstanceFleetTimeline"
    ]
    """<p>Provides historical timestamps for the instance fleet, including the time of creation, the time it became ready to run jobs, and the time of termination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceFleetStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_emr.types.instance_fleet_state

        out["State"] = aws_sdk_emr.types.instance_fleet_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        import aws_sdk_emr.types.instance_fleet_state_change_reason

        out["StateChangeReason"] = (
            aws_sdk_emr.types.instance_fleet_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "timeline" in value:
        import aws_sdk_emr.types.instance_fleet_timeline

        out["Timeline"] = (
            aws_sdk_emr.types.instance_fleet_timeline.serialize_aws_json_1_1(
                value["timeline"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceFleetStatus:
    out: InstanceFleetStatus = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_emr.types.instance_fleet_state

        out["state"] = aws_sdk_emr.types.instance_fleet_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StateChangeReason" in data:
        import aws_sdk_emr.types.instance_fleet_state_change_reason

        out["state_change_reason"] = (
            aws_sdk_emr.types.instance_fleet_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if "Timeline" in data:
        import aws_sdk_emr.types.instance_fleet_timeline

        out["timeline"] = (
            aws_sdk_emr.types.instance_fleet_timeline.deserialize_aws_json_1_1(
                data["Timeline"]
            )
        )
    return out
