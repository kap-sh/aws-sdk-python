"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationTranscriptPointOfInterest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets
    import capo_connect.types.evaluation_suggested_answer_transcript_segment


class EvaluationTranscriptPointOfInterest(TypedDict, closed=True):
    millisecond_offsets: NotRequired[
        "capo_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets.EvaluationSuggestedAnswerTranscriptMillisecondOffsets"
    ]
    """<p>Offset in milliseconds from the beginning of transcript.</p>"""
    transcript_segment: NotRequired[
        "capo_connect.types.evaluation_suggested_answer_transcript_segment.EvaluationSuggestedAnswerTranscriptSegment"
    ]
    """<p>Segment of transcript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationTranscriptPointOfInterest) -> dict:
    out: dict = {}
    if "millisecond_offsets" in value:
        import capo_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets

        out["MillisecondOffsets"] = (
            capo_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets.serialize_json(
                value["millisecond_offsets"]
            )
        )
    if "transcript_segment" in value:
        out["TranscriptSegment"] = value["transcript_segment"]
    return out


def deserialize_json(data: dict) -> EvaluationTranscriptPointOfInterest:
    out: EvaluationTranscriptPointOfInterest = {}  # type: ignore[typeddict-item]
    if "MillisecondOffsets" in data:
        import capo_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets

        out["millisecond_offsets"] = (
            capo_connect.types.evaluation_suggested_answer_transcript_millisecond_offsets.deserialize_json(
                data["MillisecondOffsets"]
            )
        )
    if "TranscriptSegment" in data:
        out["transcript_segment"] = data["TranscriptSegment"]
    return out
