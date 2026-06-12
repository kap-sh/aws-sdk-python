"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribePatientContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.pronouns


class MedicalScribePatientContext(TypedDict):
    pronouns: NotRequired["aws_sdk_transcribe_streaming.types.pronouns.Pronouns"]
    """<p>The patient's preferred pronouns that the user wants to provide as a context for clinical note generation .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePatientContext) -> dict:
    out: dict = {}
    if "pronouns" in value:
        import aws_sdk_transcribe_streaming.types.pronouns

        out["Pronouns"] = aws_sdk_transcribe_streaming.types.pronouns.serialize_json(
            value["pronouns"]
        )
    return out


def deserialize_json(data: dict) -> MedicalScribePatientContext:
    out: MedicalScribePatientContext = {}  # type: ignore[typeddict-item]
    if "Pronouns" in data:
        import aws_sdk_transcribe_streaming.types.pronouns

        out["pronouns"] = aws_sdk_transcribe_streaming.types.pronouns.deserialize_json(
            data["Pronouns"]
        )
    return out
