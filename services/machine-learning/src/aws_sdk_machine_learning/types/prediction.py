"""Generated from Smithy shape ``com.amazonaws.machinelearning#Prediction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.details_map
    import aws_sdk_machine_learning.types.float_label
    import aws_sdk_machine_learning.types.label
    import aws_sdk_machine_learning.types.score_value_per_label_map


class Prediction(TypedDict):
    predicted_label: NotRequired["aws_sdk_machine_learning.types.label.Label"]
    """<p>The prediction label for either a <code>BINARY</code> or <code>MULTICLASS</code> <code>MLModel</code>.</p>"""
    predicted_value: NotRequired[
        "aws_sdk_machine_learning.types.float_label.floatLabel"
    ]
    """<p>The prediction value for <code>REGRESSION</code> <code>MLModel</code>.</p>"""
    predicted_scores: NotRequired[
        "aws_sdk_machine_learning.types.score_value_per_label_map.ScoreValuePerLabelMap"
    ]
    details: NotRequired["aws_sdk_machine_learning.types.details_map.DetailsMap"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Prediction) -> dict:
    out: dict = {}
    if "predicted_label" in value:
        out["predictedLabel"] = value["predicted_label"]
    if "predicted_value" in value:
        out["predictedValue"] = value["predicted_value"]
    if "predicted_scores" in value:
        import aws_sdk_machine_learning.types.score_value_per_label_map

        out["predictedScores"] = (
            aws_sdk_machine_learning.types.score_value_per_label_map.serialize_aws_json_1_1(
                value["predicted_scores"]
            )
        )
    if "details" in value:
        import aws_sdk_machine_learning.types.details_map

        out["details"] = (
            aws_sdk_machine_learning.types.details_map.serialize_aws_json_1_1(
                value["details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Prediction:
    out: Prediction = {}  # type: ignore[typeddict-item]
    if "predictedLabel" in data:
        out["predicted_label"] = data["predictedLabel"]
    if "predictedValue" in data:
        out["predicted_value"] = data["predictedValue"]
    if "predictedScores" in data:
        import aws_sdk_machine_learning.types.score_value_per_label_map

        out["predicted_scores"] = (
            aws_sdk_machine_learning.types.score_value_per_label_map.deserialize_aws_json_1_1(
                data["predictedScores"]
            )
        )
    if "details" in data:
        import aws_sdk_machine_learning.types.details_map

        out["details"] = (
            aws_sdk_machine_learning.types.details_map.deserialize_aws_json_1_1(
                data["details"]
            )
        )
    return out
