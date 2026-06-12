"""Generated from Smithy shape ``com.amazonaws.workspaces#CapacityStatus``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.active_user_sessions
    import aws_sdk_workspaces.types.actual_user_sessions
    import aws_sdk_workspaces.types.available_user_sessions
    import aws_sdk_workspaces.types.desired_user_sessions


class CapacityStatus(TypedDict):
    available_user_sessions: (
        "aws_sdk_workspaces.types.available_user_sessions.AvailableUserSessions"
    )
    """<p>The number of user sessions currently available for streaming from your pool.</p> <p>AvailableUserSessions = ActualUserSessions - ActiveUserSessions</p>"""
    desired_user_sessions: (
        "aws_sdk_workspaces.types.desired_user_sessions.DesiredUserSessions"
    )
    """<p>The total number of sessions slots that are either running or pending. This represents the total number of concurrent streaming sessions your pool can support in a steady state.</p>"""
    actual_user_sessions: (
        "aws_sdk_workspaces.types.actual_user_sessions.ActualUserSessions"
    )
    """<p>The total number of user sessions that are available for streaming or are currently streaming in your pool.</p> <p>ActualUserSessions = AvailableUserSessions + ActiveUserSessions</p>"""
    active_user_sessions: (
        "aws_sdk_workspaces.types.active_user_sessions.ActiveUserSessions"
    )
    """<p>The number of user sessions currently being used for your pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityStatus) -> dict:
    out: dict = {}
    out["AvailableUserSessions"] = value["available_user_sessions"]
    out["DesiredUserSessions"] = value["desired_user_sessions"]
    out["ActualUserSessions"] = value["actual_user_sessions"]
    out["ActiveUserSessions"] = value["active_user_sessions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityStatus:
    out: CapacityStatus = {}  # type: ignore[typeddict-item]
    if "AvailableUserSessions" in data:
        out["available_user_sessions"] = data["AvailableUserSessions"]
    else:
        raise DeserializationError("CapacityStatus.available_user_sessions required")
    if "DesiredUserSessions" in data:
        out["desired_user_sessions"] = data["DesiredUserSessions"]
    else:
        raise DeserializationError("CapacityStatus.desired_user_sessions required")
    if "ActualUserSessions" in data:
        out["actual_user_sessions"] = data["ActualUserSessions"]
    else:
        raise DeserializationError("CapacityStatus.actual_user_sessions required")
    if "ActiveUserSessions" in data:
        out["active_user_sessions"] = data["ActiveUserSessions"]
    else:
        raise DeserializationError("CapacityStatus.active_user_sessions required")
    return out
