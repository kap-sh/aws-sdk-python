"""Generated from Smithy shape ``com.amazonaws.emrserverless#StartSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.session_arn
    import capo_emr_serverless.types.session_id


class StartSessionResponse(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The output contains the application ID on which the session was started.</p>"""
    session_id: "capo_emr_serverless.types.session_id.SessionId"
    """<p>The output contains the ID of the session.</p>"""
    arn: "capo_emr_serverless.types.session_arn.SessionArn"
    """<p>The output contains the ARN of the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSessionResponse) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["sessionId"] = value["session_id"]
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> StartSessionResponse:
    out: StartSessionResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    else:
        raise DeserializationError("StartSessionResponse.application_id required")
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("StartSessionResponse.session_id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("StartSessionResponse.arn required")
    return out
