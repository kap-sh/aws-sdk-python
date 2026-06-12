"""Generated from Smithy shape ``com.amazonaws.ssm#ResumeSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.session_id


class ResumeSessionRequest(TypedDict):
    session_id: "aws_sdk_ssm.types.session_id.SessionId"
    """<p>The ID of the disconnected session to resume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResumeSessionRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResumeSessionRequest:
    out: ResumeSessionRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError("ResumeSessionRequest.session_id required")
    return out
