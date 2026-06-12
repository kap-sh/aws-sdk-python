"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityTypesEvaluationMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.double


class EntityTypesEvaluationMetrics(TypedDict):
    precision: NotRequired["aws_sdk_comprehend.types.double.Double"]
    """<p>A measure of the usefulness of the recognizer results for a specific entity type in the test data. High precision means that the recognizer returned substantially more relevant results than irrelevant ones. </p>"""
    recall: NotRequired["aws_sdk_comprehend.types.double.Double"]
    """<p>A measure of how complete the recognizer results are for a specific entity type in the test data. High recall means that the recognizer returned most of the relevant results.</p>"""
    f1_score: NotRequired["aws_sdk_comprehend.types.double.Double"]
    """<p>A measure of how accurate the recognizer results are for a specific entity type in the test data. It is derived from the <code>Precision</code> and <code>Recall</code> values. The <code>F1Score</code> is the harmonic average of the two scores. The highest score is 1, and the worst score is 0. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityTypesEvaluationMetrics) -> dict:
    out: dict = {}
    if "precision" in value:
        out["Precision"] = value["precision"]
    if "recall" in value:
        out["Recall"] = value["recall"]
    if "f1_score" in value:
        out["F1Score"] = value["f1_score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityTypesEvaluationMetrics:
    out: EntityTypesEvaluationMetrics = {}  # type: ignore[typeddict-item]
    if "Precision" in data:
        out["precision"] = data["Precision"]
    if "Recall" in data:
        out["recall"] = data["Recall"]
    if "F1Score" in data:
        out["f1_score"] = data["F1Score"]
    return out
