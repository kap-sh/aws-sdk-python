"""Generated from Smithy shape ``com.amazonaws.transcribe#SubtitleFileUris``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.uri

SubtitleFileUris: TypeAlias = list["capo_transcribe.types.uri.Uri"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubtitleFileUris) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubtitleFileUris:
    return list(data)
