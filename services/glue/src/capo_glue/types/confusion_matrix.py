"""Generated from Smithy shape ``com.amazonaws.glue#ConfusionMatrix``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.records_count


class ConfusionMatrix(TypedDict, closed=True):
    num_true_positives: NotRequired["capo_glue.types.records_count.RecordsCount"]
    """<p>The number of matches in the data that the transform correctly found, in the confusion matrix for your transform.</p>"""
    num_false_positives: NotRequired["capo_glue.types.records_count.RecordsCount"]
    """<p>The number of nonmatches in the data that the transform incorrectly classified as a match, in the confusion matrix for your transform.</p>"""
    num_true_negatives: NotRequired["capo_glue.types.records_count.RecordsCount"]
    """<p>The number of nonmatches in the data that the transform correctly rejected, in the confusion matrix for your transform.</p>"""
    num_false_negatives: NotRequired["capo_glue.types.records_count.RecordsCount"]
    """<p>The number of matches in the data that the transform didn't find, in the confusion matrix for your transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfusionMatrix) -> dict:
    out: dict = {}
    if "num_true_positives" in value:
        out["NumTruePositives"] = value["num_true_positives"]
    if "num_false_positives" in value:
        out["NumFalsePositives"] = value["num_false_positives"]
    if "num_true_negatives" in value:
        out["NumTrueNegatives"] = value["num_true_negatives"]
    if "num_false_negatives" in value:
        out["NumFalseNegatives"] = value["num_false_negatives"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfusionMatrix:
    out: ConfusionMatrix = {}  # type: ignore[typeddict-item]
    if "NumTruePositives" in data:
        out["num_true_positives"] = data["NumTruePositives"]
    if "NumFalsePositives" in data:
        out["num_false_positives"] = data["NumFalsePositives"]
    if "NumTrueNegatives" in data:
        out["num_true_negatives"] = data["NumTrueNegatives"]
    if "NumFalseNegatives" in data:
        out["num_false_negatives"] = data["NumFalseNegatives"]
    return out
