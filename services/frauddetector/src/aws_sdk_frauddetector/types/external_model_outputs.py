"""Generated from Smithy shape ``com.amazonaws.frauddetector#ExternalModelOutputs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.external_model_prediction_map
    import aws_sdk_frauddetector.types.external_model_summary


class ExternalModelOutputs(TypedDict, closed=True):
    external_model: NotRequired[
        "aws_sdk_frauddetector.types.external_model_summary.ExternalModelSummary"
    ]
    """<p>The Amazon SageMaker model.</p>"""
    outputs: NotRequired[
        "aws_sdk_frauddetector.types.external_model_prediction_map.ExternalModelPredictionMap"
    ]
    """<p>The fraud prediction scores from Amazon SageMaker model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalModelOutputs) -> dict:
    out: dict = {}
    if "external_model" in value:
        import aws_sdk_frauddetector.types.external_model_summary

        out["externalModel"] = (
            aws_sdk_frauddetector.types.external_model_summary.serialize_aws_json_1_1(
                value["external_model"]
            )
        )
    if "outputs" in value:
        import aws_sdk_frauddetector.types.external_model_prediction_map

        out["outputs"] = (
            aws_sdk_frauddetector.types.external_model_prediction_map.serialize_aws_json_1_1(
                value["outputs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalModelOutputs:
    out: ExternalModelOutputs = {}  # type: ignore[typeddict-item]
    if "externalModel" in data:
        import aws_sdk_frauddetector.types.external_model_summary

        out["external_model"] = (
            aws_sdk_frauddetector.types.external_model_summary.deserialize_aws_json_1_1(
                data["externalModel"]
            )
        )
    if "outputs" in data:
        import aws_sdk_frauddetector.types.external_model_prediction_map

        out["outputs"] = (
            aws_sdk_frauddetector.types.external_model_prediction_map.deserialize_aws_json_1_1(
                data["outputs"]
            )
        )
    return out
