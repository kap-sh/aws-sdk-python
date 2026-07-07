"""Generated from Smithy shape ``com.amazonaws.ssm#TerminateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.session_id


class TerminateSessionRequest(TypedDict, closed=True):
    session_id: "aws_sdk_ssm.types.session_id.SessionId"
    """<p>The ID of the session to terminate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateSessionRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateSessionRequest:
    out: TerminateSessionRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError("TerminateSessionRequest.session_id required")
    return out
