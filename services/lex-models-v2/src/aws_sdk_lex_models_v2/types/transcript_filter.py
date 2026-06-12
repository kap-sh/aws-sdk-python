"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TranscriptFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.lex_transcript_filter


class TranscriptFilter(TypedDict):
    lex_transcript_filter: NotRequired[
        "aws_sdk_lex_models_v2.types.lex_transcript_filter.LexTranscriptFilter"
    ]
    """<p>The object representing the filter that Amazon Lex will use to select the appropriate transcript when the transcript format is the Amazon Lex format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptFilter) -> dict:
    out: dict = {}
    if "lex_transcript_filter" in value:
        import aws_sdk_lex_models_v2.types.lex_transcript_filter

        out["lexTranscriptFilter"] = (
            aws_sdk_lex_models_v2.types.lex_transcript_filter.serialize_json(
                value["lex_transcript_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> TranscriptFilter:
    out: TranscriptFilter = {}  # type: ignore[typeddict-item]
    if "lexTranscriptFilter" in data:
        import aws_sdk_lex_models_v2.types.lex_transcript_filter

        out["lex_transcript_filter"] = (
            aws_sdk_lex_models_v2.types.lex_transcript_filter.deserialize_json(
                data["lexTranscriptFilter"]
            )
        )
    return out
