"""Generated from Smithy shape ``com.amazonaws.appstream#ComputeCapacity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.integer


class ComputeCapacity(TypedDict, closed=True):
    desired_instances: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The desired number of streaming instances.</p>"""
    desired_sessions: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The desired number of user sessions for a multi-session fleet. This is not allowed for single-session fleets.</p> <p>When you create a fleet, you must set either the DesiredSessions or DesiredInstances attribute, based on the type of fleet you create. You can’t define both attributes or leave both attributes blank.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeCapacity) -> dict:
    out: dict = {}
    if "desired_instances" in value:
        out["DesiredInstances"] = value["desired_instances"]
    if "desired_sessions" in value:
        out["DesiredSessions"] = value["desired_sessions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeCapacity:
    out: ComputeCapacity = {}  # type: ignore[typeddict-item]
    if "DesiredInstances" in data:
        out["desired_instances"] = data["DesiredInstances"]
    if "DesiredSessions" in data:
        out["desired_sessions"] = data["DesiredSessions"]
    return out
