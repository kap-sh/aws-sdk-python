"""Generated from Smithy shape ``com.amazonaws.rekognition#GetFaceLivenessSessionResultsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.liveness_session_id


class GetFaceLivenessSessionResultsRequest(TypedDict):
    session_id: "aws_sdk_rekognition.types.liveness_session_id.LivenessSessionId"
    """<p>A unique 128-bit UUID. This is used to uniquely identify the session and also acts as an idempotency token for all operations associated with the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFaceLivenessSessionResultsRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFaceLivenessSessionResultsRequest:
    out: GetFaceLivenessSessionResultsRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError(
            "GetFaceLivenessSessionResultsRequest.session_id required"
        )
    return out
