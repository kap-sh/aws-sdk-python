"""Generated from Smithy shape ``com.amazonaws.drs#ParticipatingServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_actions_status
    import aws_sdk_drs.types.launch_status
    import aws_sdk_drs.types.recovery_instance_id
    import aws_sdk_drs.types.source_server_id


class ParticipatingServer(TypedDict, closed=True):
    source_server_id: NotRequired["aws_sdk_drs.types.source_server_id.SourceServerID"]
    """<p>The Source Server ID of a participating server.</p>"""
    recovery_instance_id: NotRequired[
        "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
    ]
    """<p>The Recovery Instance ID of a participating server.</p>"""
    launch_status: NotRequired["aws_sdk_drs.types.launch_status.LaunchStatus"]
    """<p>The launch status of a participating server.</p>"""
    launch_actions_status: NotRequired[
        "aws_sdk_drs.types.launch_actions_status.LaunchActionsStatus"
    ]
    """<p>The post-launch action runs of a participating server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingServer) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "recovery_instance_id" in value:
        out["recoveryInstanceID"] = value["recovery_instance_id"]
    if "launch_status" in value:
        out["launchStatus"] = value["launch_status"]
    if "launch_actions_status" in value:
        import aws_sdk_drs.types.launch_actions_status

        out["launchActionsStatus"] = (
            aws_sdk_drs.types.launch_actions_status.serialize_json(
                value["launch_actions_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParticipatingServer:
    out: ParticipatingServer = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    if "recoveryInstanceID" in data:
        out["recovery_instance_id"] = data["recoveryInstanceID"]
    if "launchStatus" in data:
        out["launch_status"] = data["launchStatus"]
    if "launchActionsStatus" in data:
        import aws_sdk_drs.types.launch_actions_status

        out["launch_actions_status"] = (
            aws_sdk_drs.types.launch_actions_status.deserialize_json(
                data["launchActionsStatus"]
            )
        )
    return out
