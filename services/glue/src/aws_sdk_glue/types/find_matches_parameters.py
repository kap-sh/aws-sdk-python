"""Generated from Smithy shape ``com.amazonaws.glue#FindMatchesParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_name_string
    import aws_sdk_glue.types.generic_bounded_double
    import aws_sdk_glue.types.nullable_boolean


class FindMatchesParameters(TypedDict, closed=True):
    primary_key_column_name: NotRequired[
        "aws_sdk_glue.types.column_name_string.ColumnNameString"
    ]
    """<p>The name of a column that uniquely identifies rows in the source table. Used to help identify matching records.</p>"""
    precision_recall_tradeoff: NotRequired[
        "aws_sdk_glue.types.generic_bounded_double.GenericBoundedDouble"
    ]
    """<p>The value selected when tuning your transform for a balance between precision and recall. A value of 0.5 means no preference; a value of 1.0 means a bias purely for precision, and a value of 0.0 means a bias for recall. Because this is a tradeoff, choosing values close to 1.0 means very low recall, and choosing values close to 0.0 results in very low precision.</p> <p>The precision metric indicates how often your model is correct when it predicts a match. </p> <p>The recall metric indicates that for an actual match, how often your model predicts the match.</p>"""
    accuracy_cost_tradeoff: NotRequired[
        "aws_sdk_glue.types.generic_bounded_double.GenericBoundedDouble"
    ]
    """<p>The value that is selected when tuning your transform for a balance between accuracy and cost. A value of 0.5 means that the system balances accuracy and cost concerns. A value of 1.0 means a bias purely for accuracy, which typically results in a higher cost, sometimes substantially higher. A value of 0.0 means a bias purely for cost, which results in a less accurate <code>FindMatches</code> transform, sometimes with unacceptable accuracy.</p> <p>Accuracy measures how well the transform finds true positives and true negatives. Increasing accuracy requires more machine resources and cost. But it also results in increased recall. </p> <p>Cost measures how many compute resources, and thus money, are consumed to run the transform.</p>"""
    enforce_provided_labels: NotRequired[
        "aws_sdk_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>The value to switch on or off to force the output to match the provided labels from users. If the value is <code>True</code>, the <code>find matches</code> transform forces the output to match the provided labels. The results override the normal conflation results. If the value is <code>False</code>, the <code>find matches</code> transform does not ensure all the labels provided are respected, and the results rely on the trained model.</p> <p>Note that setting this value to true may increase the conflation execution time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FindMatchesParameters) -> dict:
    out: dict = {}
    if "primary_key_column_name" in value:
        out["PrimaryKeyColumnName"] = value["primary_key_column_name"]
    if "precision_recall_tradeoff" in value:
        out["PrecisionRecallTradeoff"] = value["precision_recall_tradeoff"]
    if "accuracy_cost_tradeoff" in value:
        out["AccuracyCostTradeoff"] = value["accuracy_cost_tradeoff"]
    if "enforce_provided_labels" in value:
        out["EnforceProvidedLabels"] = value["enforce_provided_labels"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FindMatchesParameters:
    out: FindMatchesParameters = {}  # type: ignore[typeddict-item]
    if "PrimaryKeyColumnName" in data:
        out["primary_key_column_name"] = data["PrimaryKeyColumnName"]
    if "PrecisionRecallTradeoff" in data:
        out["precision_recall_tradeoff"] = data["PrecisionRecallTradeoff"]
    if "AccuracyCostTradeoff" in data:
        out["accuracy_cost_tradeoff"] = data["AccuracyCostTradeoff"]
    if "EnforceProvidedLabels" in data:
        out["enforce_provided_labels"] = data["EnforceProvidedLabels"]
    return out
