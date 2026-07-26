"""Generated from Smithy shape ``com.amazonaws.transcribe#Words``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.word

Words: TypeAlias = list["capo_transcribe.types.word.Word"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Words) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Words:
    return list(data)
