"""Generated from Smithy shape ``com.amazonaws.frauddetector#TrainingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.data_validation_metrics
    import aws_sdk_frauddetector.types.training_metrics
    import aws_sdk_frauddetector.types.variable_importance_metrics


class TrainingResult(TypedDict, closed=True):
    data_validation_metrics: NotRequired[
        "aws_sdk_frauddetector.types.data_validation_metrics.DataValidationMetrics"
    ]
    """<p>The validation metrics.</p>"""
    training_metrics: NotRequired[
        "aws_sdk_frauddetector.types.training_metrics.TrainingMetrics"
    ]
    """<p>The training metric details.</p>"""
    variable_importance_metrics: NotRequired[
        "aws_sdk_frauddetector.types.variable_importance_metrics.VariableImportanceMetrics"
    ]
    """<p>The variable importance metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingResult) -> dict:
    out: dict = {}
    if "data_validation_metrics" in value:
        import aws_sdk_frauddetector.types.data_validation_metrics

        out["dataValidationMetrics"] = (
            aws_sdk_frauddetector.types.data_validation_metrics.serialize_aws_json_1_1(
                value["data_validation_metrics"]
            )
        )
    if "training_metrics" in value:
        import aws_sdk_frauddetector.types.training_metrics

        out["trainingMetrics"] = (
            aws_sdk_frauddetector.types.training_metrics.serialize_aws_json_1_1(
                value["training_metrics"]
            )
        )
    if "variable_importance_metrics" in value:
        import aws_sdk_frauddetector.types.variable_importance_metrics

        out["variableImportanceMetrics"] = (
            aws_sdk_frauddetector.types.variable_importance_metrics.serialize_aws_json_1_1(
                value["variable_importance_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingResult:
    out: TrainingResult = {}  # type: ignore[typeddict-item]
    if "dataValidationMetrics" in data:
        import aws_sdk_frauddetector.types.data_validation_metrics

        out["data_validation_metrics"] = (
            aws_sdk_frauddetector.types.data_validation_metrics.deserialize_aws_json_1_1(
                data["dataValidationMetrics"]
            )
        )
    if "trainingMetrics" in data:
        import aws_sdk_frauddetector.types.training_metrics

        out["training_metrics"] = (
            aws_sdk_frauddetector.types.training_metrics.deserialize_aws_json_1_1(
                data["trainingMetrics"]
            )
        )
    if "variableImportanceMetrics" in data:
        import aws_sdk_frauddetector.types.variable_importance_metrics

        out["variable_importance_metrics"] = (
            aws_sdk_frauddetector.types.variable_importance_metrics.deserialize_aws_json_1_1(
                data["variableImportanceMetrics"]
            )
        )
    return out
