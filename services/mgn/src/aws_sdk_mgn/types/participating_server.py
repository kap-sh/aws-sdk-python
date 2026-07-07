"""Generated from Smithy shape ``com.amazonaws.mgn#ParticipatingServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.ec2_instance_id
    import aws_sdk_mgn.types.launch_status
    import aws_sdk_mgn.types.post_launch_actions_status
    import aws_sdk_mgn.types.source_server_id


class ParticipatingServer(TypedDict, closed=True):
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>Participating server Source Server ID.</p>"""
    launch_status: NotRequired["aws_sdk_mgn.types.launch_status.LaunchStatus"]
    """<p>Participating server launch status.</p>"""
    launched_ec2_instance_id: NotRequired[
        "aws_sdk_mgn.types.ec2_instance_id.EC2InstanceID"
    ]
    """<p>Participating server's launched ec2 instance ID.</p>"""
    post_launch_actions_status: NotRequired[
        "aws_sdk_mgn.types.post_launch_actions_status.PostLaunchActionsStatus"
    ]
    """<p>Participating server's Post Launch Actions Status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingServer) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "launch_status" in value:
        out["launchStatus"] = value["launch_status"]
    if "launched_ec2_instance_id" in value:
        out["launchedEc2InstanceID"] = value["launched_ec2_instance_id"]
    if "post_launch_actions_status" in value:
        import aws_sdk_mgn.types.post_launch_actions_status

        out["postLaunchActionsStatus"] = (
            aws_sdk_mgn.types.post_launch_actions_status.serialize_json(
                value["post_launch_actions_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParticipatingServer:
    out: ParticipatingServer = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError("ParticipatingServer.source_server_id required")
    if "launchStatus" in data:
        out["launch_status"] = data["launchStatus"]
    if "launchedEc2InstanceID" in data:
        out["launched_ec2_instance_id"] = data["launchedEc2InstanceID"]
    if "postLaunchActionsStatus" in data:
        import aws_sdk_mgn.types.post_launch_actions_status

        out["post_launch_actions_status"] = (
            aws_sdk_mgn.types.post_launch_actions_status.deserialize_json(
                data["postLaunchActionsStatus"]
            )
        )
    return out
