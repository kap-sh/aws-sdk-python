"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationTranscriptPointOfInterest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets
    import aws_sdk_connect.types.evaluation_suggested_answer_transcript_segment


class EvaluationTranscriptPointOfInterest(TypedDict):
    millisecond_offsets: NotRequired[
        "aws_sdk_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets.EvaluationSuggestedAnswerTranscriptMillisecondOffsets"
    ]
    """<p>Offset in milliseconds from the beginning of transcript.</p>"""
    transcript_segment: NotRequired[
        "aws_sdk_connect.types.evaluation_suggested_answer_transcript_segment.EvaluationSuggestedAnswerTranscriptSegment"
    ]
    """<p>Segment of transcript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationTranscriptPointOfInterest) -> dict:
    out: dict = {}
    if "millisecond_offsets" in value:
        import aws_sdk_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets

        out["MillisecondOffsets"] = (
            aws_sdk_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets.serialize_json(
                value["millisecond_offsets"]
            )
        )
    if "transcript_segment" in value:
        out["TranscriptSegment"] = value["transcript_segment"]
    return out


def deserialize_json(data: dict) -> EvaluationTranscriptPointOfInterest:
    out: EvaluationTranscriptPointOfInterest = {}  # type: ignore[typeddict-item]
    if "MillisecondOffsets" in data:
        import aws_sdk_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets

        out["millisecond_offsets"] = (
            aws_sdk_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets.deserialize_json(
                data["MillisecondOffsets"]
            )
        )
    if "TranscriptSegment" in data:
        out["transcript_segment"] = data["TranscriptSegment"]
    return out
