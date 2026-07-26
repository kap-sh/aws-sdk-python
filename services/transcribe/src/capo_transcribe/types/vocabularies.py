"""Generated from Smithy shape ``com.amazonaws.transcribe#Vocabularies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.vocabulary_info

Vocabularies: TypeAlias = list["capo_transcribe.types.vocabulary_info.VocabularyInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Vocabularies) -> list:
    import capo_transcribe.types.vocabulary_info

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.vocabulary_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Vocabularies:
    import capo_transcribe.types.vocabulary_info

    out: Vocabularies = []
    for item in data:
        out.append(capo_transcribe.types.vocabulary_info.deserialize_aws_json_1_1(item))
    return out
