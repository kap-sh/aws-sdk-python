"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribePatientContext``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.pronouns


class MedicalScribePatientContext(TypedDict):
    pronouns: NotRequired["aws_sdk_transcribe.types.pronouns.Pronouns"]
    """<p>The patient's preferred pronouns that the user wants to provide as a context for clinical note generation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribePatientContext) -> dict:
    out: dict = {}
    if "pronouns" in value:
        import aws_sdk_transcribe.types.pronouns

        out["Pronouns"] = aws_sdk_transcribe.types.pronouns.serialize_aws_json_1_1(
            value["pronouns"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribePatientContext:
    out: MedicalScribePatientContext = {}  # type: ignore[typeddict-item]
    if "Pronouns" in data:
        import aws_sdk_transcribe.types.pronouns

        out["pronouns"] = aws_sdk_transcribe.types.pronouns.deserialize_aws_json_1_1(
            data["Pronouns"]
        )
    return out
