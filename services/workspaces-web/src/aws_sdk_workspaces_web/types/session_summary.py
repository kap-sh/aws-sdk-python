"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.session_status
    import aws_sdk_workspaces_web.types.string_type
    import aws_sdk_workspaces_web.types.timestamp
    import aws_sdk_workspaces_web.types.username


class SessionSummary(TypedDict):
    portal_arn: NotRequired["aws_sdk_workspaces_web.types.arn.ARN"]
    """<p>The ARN of the web portal.</p>"""
    session_id: NotRequired["aws_sdk_workspaces_web.types.string_type.StringType"]
    """<p>The ID of the session.</p>"""
    username: NotRequired["aws_sdk_workspaces_web.types.username.Username"]
    """<p>The username of the session.</p>"""
    status: NotRequired["aws_sdk_workspaces_web.types.session_status.SessionStatus"]
    """<p>The status of the session.</p>"""
    start_time: NotRequired["aws_sdk_workspaces_web.types.timestamp.Timestamp"]
    """<p>The start time of the session.</p>"""
    end_time: NotRequired["aws_sdk_workspaces_web.types.timestamp.Timestamp"]
    """<p>The end time of the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    if "portal_arn" in value:
        out["portalArn"] = value["portal_arn"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "username" in value:
        out["username"] = value["username"]
    if "status" in value:
        import aws_sdk_workspaces_web.types.session_status

        out["status"] = aws_sdk_workspaces_web.types.session_status.serialize_json(
            value["status"]
        )
    if "start_time" in value:
        import aws_sdk_workspaces_web.types.timestamp

        out["startTime"] = aws_sdk_workspaces_web.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_workspaces_web.types.timestamp

        out["endTime"] = aws_sdk_workspaces_web.types.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "username" in data:
        out["username"] = data["username"]
    if "status" in data:
        import aws_sdk_workspaces_web.types.session_status

        out["status"] = aws_sdk_workspaces_web.types.session_status.deserialize_json(
            data["status"]
        )
    if "startTime" in data:
        import aws_sdk_workspaces_web.types.timestamp

        out["start_time"] = aws_sdk_workspaces_web.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_workspaces_web.types.timestamp

        out["end_time"] = aws_sdk_workspaces_web.types.timestamp.deserialize_json(
            data["endTime"]
        )
    return out
