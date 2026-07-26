"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalTranscript``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_result_list


class MedicalTranscript(TypedDict, closed=True):
    results: NotRequired[
        "capo_transcribe_streaming.types.medical_result_list.MedicalResultList"
    ]
    """<p>Contains a set of transcription results from one or more audio segments, along with additional information per your request parameters. This can include information relating to alternative transcriptions, channel identification, partial result stabilization, language identification, and other transcription-related data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalTranscript) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_transcribe_streaming.types.medical_result_list

        out["Results"] = (
            capo_transcribe_streaming.types.medical_result_list.serialize_json(
                value["results"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalTranscript:
    out: MedicalTranscript = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_transcribe_streaming.types.medical_result_list

        out["results"] = (
            capo_transcribe_streaming.types.medical_result_list.deserialize_json(
                data["Results"]
            )
        )
    return out
