"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#GetMedicalScribeStreamRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.session_id


class GetMedicalScribeStreamRequest(TypedDict):
    session_id: "aws_sdk_transcribe_streaming.types.session_id.SessionId"
    """<p>The identifier of the HealthScribe streaming session you want information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalScribeStreamRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMedicalScribeStreamRequest:
    out: GetMedicalScribeStreamRequest = {}  # type: ignore[typeddict-item]
    return out
