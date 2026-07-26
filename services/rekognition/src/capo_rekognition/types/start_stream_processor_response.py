"""Generated from Smithy shape ``com.amazonaws.rekognition#StartStreamProcessorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.start_stream_processor_session_id


class StartStreamProcessorResponse(TypedDict, closed=True):
    session_id: NotRequired[
        "capo_rekognition.types.start_stream_processor_session_id.StartStreamProcessorSessionId"
    ]
    """<p> A unique identifier for the stream processing session. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartStreamProcessorResponse) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartStreamProcessorResponse:
    out: StartStreamProcessorResponse = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    return out
