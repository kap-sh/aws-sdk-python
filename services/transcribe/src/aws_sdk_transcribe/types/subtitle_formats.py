"""Generated from Smithy shape ``com.amazonaws.transcribe#SubtitleFormats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.subtitle_format

SubtitleFormats: TypeAlias = list[
    "aws_sdk_transcribe.types.subtitle_format.SubtitleFormat"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubtitleFormats) -> list:
    import aws_sdk_transcribe.types.subtitle_format

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe.types.subtitle_format.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SubtitleFormats:
    import aws_sdk_transcribe.types.subtitle_format

    out: SubtitleFormats = []
    for item in data:
        out.append(
            aws_sdk_transcribe.types.subtitle_format.deserialize_aws_json_1_1(item)
        )
    return out
