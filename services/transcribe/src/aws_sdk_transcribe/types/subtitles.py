"""Generated from Smithy shape ``com.amazonaws.transcribe#Subtitles``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.subtitle_formats
    import aws_sdk_transcribe.types.subtitle_output_start_index


class Subtitles(TypedDict, closed=True):
    formats: NotRequired["aws_sdk_transcribe.types.subtitle_formats.SubtitleFormats"]
    """<p>Specify the output format for your subtitle file; if you select both WebVTT (<code>vtt</code>) and SubRip (<code>srt</code>) formats, two output files are generated.</p>"""
    output_start_index: NotRequired[
        "aws_sdk_transcribe.types.subtitle_output_start_index.SubtitleOutputStartIndex"
    ]
    """<p>Specify the starting value that is assigned to the first subtitle segment.</p> <p>The default start index for Amazon Transcribe is <code>0</code>, which differs from the more widely used standard of <code>1</code>. If you're uncertain which value to use, we recommend choosing <code>1</code>, as this may improve compatibility with other services.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subtitles) -> dict:
    out: dict = {}
    if "formats" in value:
        import aws_sdk_transcribe.types.subtitle_formats

        out["Formats"] = (
            aws_sdk_transcribe.types.subtitle_formats.serialize_aws_json_1_1(
                value["formats"]
            )
        )
    if "output_start_index" in value:
        out["OutputStartIndex"] = value["output_start_index"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Subtitles:
    out: Subtitles = {}  # type: ignore[typeddict-item]
    if "Formats" in data:
        import aws_sdk_transcribe.types.subtitle_formats

        out["formats"] = (
            aws_sdk_transcribe.types.subtitle_formats.deserialize_aws_json_1_1(
                data["Formats"]
            )
        )
    if "OutputStartIndex" in data:
        out["output_start_index"] = data["OutputStartIndex"]
    return out
