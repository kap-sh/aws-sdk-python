"""Generated from Smithy shape ``com.amazonaws.appstream#ComputeCapacityStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.integer


class ComputeCapacityStatus(TypedDict, closed=True):
    desired: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The desired number of streaming instances.</p>"""
    running: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The total number of simultaneous streaming instances that are running.</p>"""
    in_use: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The number of instances in use for streaming.</p>"""
    available: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The number of currently available instances that can be used to stream sessions.</p>"""
    desired_user_sessions: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The total number of sessions slots that are either running or pending. This represents the total number of concurrent streaming sessions your fleet can support in a steady state.</p> <p>DesiredUserSessionCapacity = ActualUserSessionCapacity + PendingUserSessionCapacity</p> <p>This only applies to multi-session fleets.</p>"""
    available_user_sessions: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The number of idle session slots currently available for user sessions.</p> <p>AvailableUserSessionCapacity = ActualUserSessionCapacity - ActiveUserSessions</p> <p>This only applies to multi-session fleets.</p>"""
    active_user_sessions: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The number of user sessions currently being used for streaming sessions. This only applies to multi-session fleets.</p>"""
    actual_user_sessions: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The total number of session slots that are available for streaming or are currently streaming.</p> <p>ActualUserSessionCapacity = AvailableUserSessionCapacity + ActiveUserSessions</p> <p>This only applies to multi-session fleets.</p>"""
    draining: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The number of instances in drain mode. This only applies to multi-session fleets.</p>"""
    drain_mode_active_user_sessions: NotRequired[
        "aws_sdk_appstream.types.integer.Integer"
    ]
    """<p>The number of active user sessions on instances in drain mode. This only applies to multi-session fleets.</p>"""
    drain_mode_unused_user_sessions: NotRequired[
        "aws_sdk_appstream.types.integer.Integer"
    ]
    """<p>The number of unused session slots on instances in drain mode that cannot be used for user session provisioning. This only applies to multi-session fleets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeCapacityStatus) -> dict:
    out: dict = {}
    if "desired" in value:
        out["Desired"] = value["desired"]
    if "running" in value:
        out["Running"] = value["running"]
    if "in_use" in value:
        out["InUse"] = value["in_use"]
    if "available" in value:
        out["Available"] = value["available"]
    if "desired_user_sessions" in value:
        out["DesiredUserSessions"] = value["desired_user_sessions"]
    if "available_user_sessions" in value:
        out["AvailableUserSessions"] = value["available_user_sessions"]
    if "active_user_sessions" in value:
        out["ActiveUserSessions"] = value["active_user_sessions"]
    if "actual_user_sessions" in value:
        out["ActualUserSessions"] = value["actual_user_sessions"]
    if "draining" in value:
        out["Draining"] = value["draining"]
    if "drain_mode_active_user_sessions" in value:
        out["DrainModeActiveUserSessions"] = value["drain_mode_active_user_sessions"]
    if "drain_mode_unused_user_sessions" in value:
        out["DrainModeUnusedUserSessions"] = value["drain_mode_unused_user_sessions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeCapacityStatus:
    out: ComputeCapacityStatus = {}  # type: ignore[typeddict-item]
    if "Desired" in data:
        out["desired"] = data["Desired"]
    if "Running" in data:
        out["running"] = data["Running"]
    if "InUse" in data:
        out["in_use"] = data["InUse"]
    if "Available" in data:
        out["available"] = data["Available"]
    if "DesiredUserSessions" in data:
        out["desired_user_sessions"] = data["DesiredUserSessions"]
    if "AvailableUserSessions" in data:
        out["available_user_sessions"] = data["AvailableUserSessions"]
    if "ActiveUserSessions" in data:
        out["active_user_sessions"] = data["ActiveUserSessions"]
    if "ActualUserSessions" in data:
        out["actual_user_sessions"] = data["ActualUserSessions"]
    if "Draining" in data:
        out["draining"] = data["Draining"]
    if "DrainModeActiveUserSessions" in data:
        out["drain_mode_active_user_sessions"] = data["DrainModeActiveUserSessions"]
    if "DrainModeUnusedUserSessions" in data:
        out["drain_mode_unused_user_sessions"] = data["DrainModeUnusedUserSessions"]
    return out
