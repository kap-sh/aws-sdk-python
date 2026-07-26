"""Generated from Smithy shape ``com.amazonaws.rekognition#EvaluationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.float
    import capo_rekognition.types.summary


class EvaluationResult(TypedDict, closed=True):
    f1_score: NotRequired["capo_rekognition.types.float.Float"]
    """<p>The F1 score for the evaluation of all labels. The F1 score metric evaluates the overall precision and recall performance of the model as a single value. A higher value indicates better precision and recall performance. A lower score indicates that precision, recall, or both are performing poorly. </p>"""
    summary: NotRequired["capo_rekognition.types.summary.Summary"]
    """<p>The S3 bucket that contains the training summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationResult) -> dict:
    out: dict = {}
    if "f1_score" in value:
        out["F1Score"] = value["f1_score"]
    if "summary" in value:
        import capo_rekognition.types.summary

        out["Summary"] = capo_rekognition.types.summary.serialize_aws_json_1_1(
            value["summary"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationResult:
    out: EvaluationResult = {}  # type: ignore[typeddict-item]
    if "F1Score" in data:
        out["f1_score"] = data["F1Score"]
    if "Summary" in data:
        import capo_rekognition.types.summary

        out["summary"] = capo_rekognition.types.summary.deserialize_aws_json_1_1(
            data["Summary"]
        )
    return out
