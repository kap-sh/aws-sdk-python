"""Generated from Smithy shape ``com.amazonaws.glue#FindMatchesMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_importance_list
    import aws_sdk_glue.types.confusion_matrix
    import aws_sdk_glue.types.generic_bounded_double


class FindMatchesMetrics(TypedDict):
    area_under_pr_curve: NotRequired[
        "aws_sdk_glue.types.generic_bounded_double.GenericBoundedDouble"
    ]
    """<p>The area under the precision/recall curve (AUPRC) is a single number measuring the overall quality of the transform, that is independent of the choice made for precision vs. recall. Higher values indicate that you have a more attractive precision vs. recall tradeoff.</p> <p>For more information, see <a href=\"https://en.wikipedia.org/wiki/Precision_and_recall\">Precision and recall</a> in Wikipedia.</p>"""
    precision: NotRequired[
        "aws_sdk_glue.types.generic_bounded_double.GenericBoundedDouble"
    ]
    """<p>The precision metric indicates when often your transform is correct when it predicts a match. Specifically, it measures how well the transform finds true positives from the total true positives possible.</p> <p>For more information, see <a href=\"https://en.wikipedia.org/wiki/Precision_and_recall\">Precision and recall</a> in Wikipedia.</p>"""
    recall: NotRequired[
        "aws_sdk_glue.types.generic_bounded_double.GenericBoundedDouble"
    ]
    """<p>The recall metric indicates that for an actual match, how often your transform predicts the match. Specifically, it measures how well the transform finds true positives from the total records in the source data.</p> <p>For more information, see <a href=\"https://en.wikipedia.org/wiki/Precision_and_recall\">Precision and recall</a> in Wikipedia.</p>"""
    f1: NotRequired["aws_sdk_glue.types.generic_bounded_double.GenericBoundedDouble"]
    """<p>The maximum F1 metric indicates the transform's accuracy between 0 and 1, where 1 is the best accuracy.</p> <p>For more information, see <a href=\"https://en.wikipedia.org/wiki/F1_score\">F1 score</a> in Wikipedia.</p>"""
    confusion_matrix: NotRequired["aws_sdk_glue.types.confusion_matrix.ConfusionMatrix"]
    """<p>The confusion matrix shows you what your transform is predicting accurately and what types of errors it is making.</p> <p>For more information, see <a href=\"https://en.wikipedia.org/wiki/Confusion_matrix\">Confusion matrix</a> in Wikipedia.</p>"""
    column_importances: NotRequired[
        "aws_sdk_glue.types.column_importance_list.ColumnImportanceList"
    ]
    """<p>A list of <code>ColumnImportance</code> structures containing column importance metrics, sorted in order of descending importance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindMatchesMetrics) -> dict:
    out: dict = {}
    if "area_under_pr_curve" in value:
        out["AreaUnderPRCurve"] = value["area_under_pr_curve"]
    if "precision" in value:
        out["Precision"] = value["precision"]
    if "recall" in value:
        out["Recall"] = value["recall"]
    if "f1" in value:
        out["F1"] = value["f1"]
    if "confusion_matrix" in value:
        import aws_sdk_glue.types.confusion_matrix

        out["ConfusionMatrix"] = (
            aws_sdk_glue.types.confusion_matrix.serialize_aws_json_1_1(
                value["confusion_matrix"]
            )
        )
    if "column_importances" in value:
        import aws_sdk_glue.types.column_importance_list

        out["ColumnImportances"] = (
            aws_sdk_glue.types.column_importance_list.serialize_aws_json_1_1(
                value["column_importances"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FindMatchesMetrics:
    out: FindMatchesMetrics = {}  # type: ignore[typeddict-item]
    if "AreaUnderPRCurve" in data:
        out["area_under_pr_curve"] = data["AreaUnderPRCurve"]
    if "Precision" in data:
        out["precision"] = data["Precision"]
    if "Recall" in data:
        out["recall"] = data["Recall"]
    if "F1" in data:
        out["f1"] = data["F1"]
    if "ConfusionMatrix" in data:
        import aws_sdk_glue.types.confusion_matrix

        out["confusion_matrix"] = (
            aws_sdk_glue.types.confusion_matrix.deserialize_aws_json_1_1(
                data["ConfusionMatrix"]
            )
        )
    if "ColumnImportances" in data:
        import aws_sdk_glue.types.column_importance_list

        out["column_importances"] = (
            aws_sdk_glue.types.column_importance_list.deserialize_aws_json_1_1(
                data["ColumnImportances"]
            )
        )
    return out
