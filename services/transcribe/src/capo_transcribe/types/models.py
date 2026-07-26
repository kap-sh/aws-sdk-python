"""Generated from Smithy shape ``com.amazonaws.transcribe#Models``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.language_model

Models: TypeAlias = list["capo_transcribe.types.language_model.LanguageModel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Models) -> list:
    import capo_transcribe.types.language_model

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.language_model.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Models:
    import capo_transcribe.types.language_model

    out: Models = []
    for item in data:
        out.append(capo_transcribe.types.language_model.deserialize_aws_json_1_1(item))
    return out
