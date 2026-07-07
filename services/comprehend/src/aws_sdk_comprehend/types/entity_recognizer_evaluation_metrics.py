"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerEvaluationMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.double


class EntityRecognizerEvaluationMetrics(TypedDict, closed=True):
    precision: NotRequired["aws_sdk_comprehend.types.double.Double"]
    """<p>A measure of the usefulness of the recognizer results in the test data. High precision means that the recognizer returned substantially more relevant results than irrelevant ones. </p>"""
    recall: NotRequired["aws_sdk_comprehend.types.double.Double"]
    """<p>A measure of how complete the recognizer results are for the test data. High recall means that the recognizer returned most of the relevant results.</p>"""
    f1_score: NotRequired["aws_sdk_comprehend.types.double.Double"]
    """<p>A measure of how accurate the recognizer results are for the test data. It is derived from the <code>Precision</code> and <code>Recall</code> values. The <code>F1Score</code> is the harmonic average of the two scores. For plain text entity recognizer models, the range is 0 to 100, where 100 is the best score. For PDF/Word entity recognizer models, the range is 0 to 1, where 1 is the best score. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerEvaluationMetrics) -> dict:
    out: dict = {}
    if "precision" in value:
        out["Precision"] = value["precision"]
    if "recall" in value:
        out["Recall"] = value["recall"]
    if "f1_score" in value:
        out["F1Score"] = value["f1_score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerEvaluationMetrics:
    out: EntityRecognizerEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if "Precision" in data:
        out["precision"] = data["Precision"]
    if "Recall" in data:
        out["recall"] = data["Recall"]
    if "F1Score" in data:
        out["f1_score"] = data["F1Score"]
    return out
