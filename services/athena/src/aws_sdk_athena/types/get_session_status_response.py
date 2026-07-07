"""Generated from Smithy shape ``com.amazonaws.athena#GetSessionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.session_id
    import aws_sdk_athena.types.session_status


class GetSessionStatusResponse(TypedDict, closed=True):
    session_id: NotRequired["aws_sdk_athena.types.session_id.SessionId"]
    """<p>The session ID.</p>"""
    status: NotRequired["aws_sdk_athena.types.session_status.SessionStatus"]
    """<p>Contains information about the status of the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionStatusResponse) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "status" in value:
        import aws_sdk_athena.types.session_status

        out["Status"] = aws_sdk_athena.types.session_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionStatusResponse:
    out: GetSessionStatusResponse = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "Status" in data:
        import aws_sdk_athena.types.session_status

        out["status"] = aws_sdk_athena.types.session_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
