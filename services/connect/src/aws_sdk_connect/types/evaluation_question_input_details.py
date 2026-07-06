"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationQuestionInputDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_transcript_type


class EvaluationQuestionInputDetails(TypedDict, closed=True):
    transcript_type: NotRequired[
        "aws_sdk_connect.types.evaluation_transcript_type.EvaluationTranscriptType"
    ]
    """<p>Transcript type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationQuestionInputDetails) -> dict:
    out: dict = {}
    if "transcript_type" in value:
        import aws_sdk_connect.types.evaluation_transcript_type

        out["TranscriptType"] = (
            aws_sdk_connect.types.evaluation_transcript_type.serialize_json(
                value["transcript_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationQuestionInputDetails:
    out: EvaluationQuestionInputDetails = {}  # type: ignore[typeddict-item]
    if "TranscriptType" in data:
        import aws_sdk_connect.types.evaluation_transcript_type

        out["transcript_type"] = (
            aws_sdk_connect.types.evaluation_transcript_type.deserialize_json(
                data["TranscriptType"]
            )
        )
    return out
