"""Generated from Smithy shape ``com.amazonaws.voiceid#EvaluateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_voice_id.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_voice_id.types.domain_id
    import aws_sdk_voice_id.types.session_name_or_id


class EvaluateSessionRequest(TypedDict, closed=True):
    domain_id: "aws_sdk_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain where the session started.</p>"""
    session_name_or_id: "aws_sdk_voice_id.types.session_name_or_id.SessionNameOrId"
    """<p>The session identifier, or name of the session, that you want to evaluate. In Voice ID integration, this is the Contact-Id.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluateSessionRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    out["SessionNameOrId"] = value["session_name_or_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EvaluateSessionRequest:
    out: EvaluateSessionRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    else:
        raise DeserializationError("EvaluateSessionRequest.domain_id required")
    if "SessionNameOrId" in data:
        out["session_name_or_id"] = data["SessionNameOrId"]
    else:
        raise DeserializationError("EvaluateSessionRequest.session_name_or_id required")
    return out
