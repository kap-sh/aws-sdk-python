"""Generated from Smithy shape ``com.amazonaws.emrserverless#TerminateSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.application_id
    import aws_sdk_emr_serverless.types.session_id


class TerminateSessionResponse(TypedDict):
    application_id: "aws_sdk_emr_serverless.types.application_id.ApplicationId"
    """<p>The output contains the application ID on which the session was terminated.</p>"""
    session_id: "aws_sdk_emr_serverless.types.session_id.SessionId"
    """<p>The output contains the ID of the terminated session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TerminateSessionResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> TerminateSessionResponse:
    out: TerminateSessionResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("TerminateSessionResponse.application_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("TerminateSessionResponse.session_id required")
    return out
