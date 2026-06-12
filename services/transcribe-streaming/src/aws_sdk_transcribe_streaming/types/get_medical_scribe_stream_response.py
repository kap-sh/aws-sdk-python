"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#GetMedicalScribeStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_scribe_stream_details


class GetMedicalScribeStreamResponse(TypedDict):
    medical_scribe_stream_details: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_stream_details.MedicalScribeStreamDetails"
    ]
    """<p>Provides details about a HealthScribe streaming session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalScribeStreamResponse) -> dict:
    out: dict = {}
    if "medical_scribe_stream_details" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_stream_details

        out["MedicalScribeStreamDetails"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_stream_details.serialize_json(
                value["medical_scribe_stream_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMedicalScribeStreamResponse:
    out: GetMedicalScribeStreamResponse = {}  # type: ignore[typeddict-item]
    if "MedicalScribeStreamDetails" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_stream_details

        out["medical_scribe_stream_details"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_stream_details.deserialize_json(
                data["MedicalScribeStreamDetails"]
            )
        )
    return out
