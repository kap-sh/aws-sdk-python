"""Generated from Smithy shape ``com.amazonaws.workspaces#Capacity``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.desired_user_sessions


class Capacity(TypedDict):
    desired_user_sessions: (
        "aws_sdk_workspaces.types.desired_user_sessions.DesiredUserSessions"
    )
    """<p>The desired number of user sessions for the WorkSpaces in the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Capacity) -> dict:
    out: dict = {}
    out["DesiredUserSessions"] = value["desired_user_sessions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Capacity:
    out: Capacity = {}  # type: ignore[typeddict-item]
    if "DesiredUserSessions" in data:
        out["desired_user_sessions"] = data["DesiredUserSessions"]
    else:
        raise DeserializationError("Capacity.desired_user_sessions required")
    return out
