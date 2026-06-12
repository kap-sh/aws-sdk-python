"""Generated from Smithy shape ``com.amazonaws.frauddetector#TrainingResultV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.aggregated_variables_importance_metrics
    import aws_sdk_frauddetector.types.data_validation_metrics
    import aws_sdk_frauddetector.types.training_metrics_v2
    import aws_sdk_frauddetector.types.variable_importance_metrics


class TrainingResultV2(TypedDict):
    data_validation_metrics: NotRequired[
        "aws_sdk_frauddetector.types.data_validation_metrics.DataValidationMetrics"
    ]
    training_metrics_v2: NotRequired[
        "aws_sdk_frauddetector.types.training_metrics_v2.TrainingMetricsV2"
    ]
    """<p> The training metric details. </p>"""
    variable_importance_metrics: NotRequired[
        "aws_sdk_frauddetector.types.variable_importance_metrics.VariableImportanceMetrics"
    ]
    aggregated_variables_importance_metrics: NotRequired[
        "aws_sdk_frauddetector.types.aggregated_variables_importance_metrics.AggregatedVariablesImportanceMetrics"
    ]
    """<p> The variable importance metrics of the aggregated variables. </p> <p>Account Takeover Insights (ATI) model uses event variables from the login data you provide to continuously calculate a set of variables (aggregated variables) based on historical events. For example, your ATI model might calculate the number of times an user has logged in using the same IP address. In this case, event variables used to derive the aggregated variables are <code>IP address</code> and <code>user</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingResultV2) -> dict:
    out: dict = {}
    if "data_validation_metrics" in value:
        import aws_sdk_frauddetector.types.data_validation_metrics

        out["dataValidationMetrics"] = (
            aws_sdk_frauddetector.types.data_validation_metrics.serialize_aws_json_1_1(
                value["data_validation_metrics"]
            )
        )
    if "training_metrics_v2" in value:
        import aws_sdk_frauddetector.types.training_metrics_v2

        out["trainingMetricsV2"] = (
            aws_sdk_frauddetector.types.training_metrics_v2.serialize_aws_json_1_1(
                value["training_metrics_v2"]
            )
        )
    if "variable_importance_metrics" in value:
        import aws_sdk_frauddetector.types.variable_importance_metrics

        out["variableImportanceMetrics"] = (
            aws_sdk_frauddetector.types.variable_importance_metrics.serialize_aws_json_1_1(
                value["variable_importance_metrics"]
            )
        )
    if "aggregated_variables_importance_metrics" in value:
        import aws_sdk_frauddetector.types.aggregated_variables_importance_metrics

        out["aggregatedVariablesImportanceMetrics"] = (
            aws_sdk_frauddetector.types.aggregated_variables_importance_metrics.serialize_aws_json_1_1(
                value["aggregated_variables_importance_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingResultV2:
    out: TrainingResultV2 = {}  # type: ignore[typeddict-item]
    if "dataValidationMetrics" in data:
        import aws_sdk_frauddetector.types.data_validation_metrics

        out["data_validation_metrics"] = (
            aws_sdk_frauddetector.types.data_validation_metrics.deserialize_aws_json_1_1(
                data["dataValidationMetrics"]
            )
        )
    if "trainingMetricsV2" in data:
        import aws_sdk_frauddetector.types.training_metrics_v2

        out["training_metrics_v2"] = (
            aws_sdk_frauddetector.types.training_metrics_v2.deserialize_aws_json_1_1(
                data["trainingMetricsV2"]
            )
        )
    if "variableImportanceMetrics" in data:
        import aws_sdk_frauddetector.types.variable_importance_metrics

        out["variable_importance_metrics"] = (
            aws_sdk_frauddetector.types.variable_importance_metrics.deserialize_aws_json_1_1(
                data["variableImportanceMetrics"]
            )
        )
    if "aggregatedVariablesImportanceMetrics" in data:
        import aws_sdk_frauddetector.types.aggregated_variables_importance_metrics

        out["aggregated_variables_importance_metrics"] = (
            aws_sdk_frauddetector.types.aggregated_variables_importance_metrics.deserialize_aws_json_1_1(
                data["aggregatedVariablesImportanceMetrics"]
            )
        )
    return out
