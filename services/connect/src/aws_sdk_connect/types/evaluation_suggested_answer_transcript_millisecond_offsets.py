"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSuggestedAnswerTranscriptMillisecondOffsets``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_suggested_answer_transcript_millis_offset


class EvaluationSuggestedAnswerTranscriptMillisecondOffsets(TypedDict, closed=True):
    begin_offset_millis: "aws_sdk_connect.types.evaluation_suggested_answer_transcript_millis_offset.EvaluationSuggestedAnswerTranscriptMillisOffset"
    """<p>Offset in milliseconds from the beginning of the transcript.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: EvaluationSuggestedAnswerTranscriptMillisecondOffsets,
) -> dict:
    out: dict = {}
    out["BeginOffsetMillis"] = value.get("begin_offset_millis", 0)
    return out


def deserialize_json(
    data: dict,
) -> EvaluationSuggestedAnswerTranscriptMillisecondOffsets:
    out: EvaluationSuggestedAnswerTranscriptMillisecondOffsets = {}  # type: ignore[typeddict-item]
    if "BeginOffsetMillis" in data:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    else:
        out["begin_offset_millis"] = 0
    return out
