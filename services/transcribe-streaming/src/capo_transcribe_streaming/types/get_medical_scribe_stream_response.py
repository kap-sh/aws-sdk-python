"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#GetMedicalScribeStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_scribe_stream_details


class GetMedicalScribeStreamResponse(TypedDict, closed=True):
    medical_scribe_stream_details: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_stream_details.MedicalScribeStreamDetails"
    ]
    """<p>Provides details about a HealthScribe streaming session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMedicalScribeStreamResponse) -> dict:
    out: dict = {}
    if "medical_scribe_stream_details" in value:
        import capo_transcribe_streaming.types.medical_scribe_stream_details

        out["MedicalScribeStreamDetails"] = (
            capo_transcribe_streaming.types.medical_scribe_stream_details.serialize_json(
                value["medical_scribe_stream_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMedicalScribeStreamResponse:
    out: GetMedicalScribeStreamResponse = {}  # type: ignore[typeddict-item]
    if "MedicalScribeStreamDetails" in data:
        import capo_transcribe_streaming.types.medical_scribe_stream_details

        out["medical_scribe_stream_details"] = (
            capo_transcribe_streaming.types.medical_scribe_stream_details.deserialize_json(
                data["MedicalScribeStreamDetails"]
            )
        )
    return out
