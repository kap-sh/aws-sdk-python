"""Generated from Smithy shape ``com.amazonaws.textract#EvaluationMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.float


class EvaluationMetric(TypedDict, closed=True):
    f1_score: "capo_textract.types.float.Float"
    """<p>The F1 score for an adapter version.</p>"""
    precision: "capo_textract.types.float.Float"
    """<p>The Precision score for an adapter version.</p>"""
    recall: "capo_textract.types.float.Float"
    """<p>The Recall score for an adapter version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationMetric) -> dict:
    out: dict = {}
    out["F1Score"] = value.get("f1_score", 0)
    out["Precision"] = value.get("precision", 0)
    out["Recall"] = value.get("recall", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationMetric:
    out: EvaluationMetric = {}  # type: ignore[typeddict-item]
    if "F1Score" in data:
        out["f1_score"] = data["F1Score"]
    else:
        out["f1_score"] = 0
    if "Precision" in data:
        out["precision"] = data["Precision"]
    else:
        out["precision"] = 0
    if "Recall" in data:
        out["recall"] = data["Recall"]
    else:
        out["recall"] = 0
    return out
