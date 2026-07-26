"""Generated from Smithy shape ``com.amazonaws.frauddetector#EvaluatedModelVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.list_of_model_version_evaluations
    import capo_frauddetector.types.string


class EvaluatedModelVersion(TypedDict, closed=True):
    model_id: NotRequired["capo_frauddetector.types.string.string"]
    """<p> The model ID. </p>"""
    model_version: NotRequired["capo_frauddetector.types.string.string"]
    """<p> The model version. </p>"""
    model_type: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The model type. </p> <p>Valid values: <code>ONLINE_FRAUD_INSIGHTS</code> | <code>TRANSACTION_FRAUD_INSIGHTS</code> </p>"""
    evaluations: NotRequired[
        "capo_frauddetector.types.list_of_model_version_evaluations.ListOfModelVersionEvaluations"
    ]
    """<p> Evaluations generated for the model version. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatedModelVersion) -> dict:
    out: dict = {}
    if "model_id" in value:
        out["modelId"] = value["model_id"]
    if "model_version" in value:
        out["modelVersion"] = value["model_version"]
    if "model_type" in value:
        out["modelType"] = value["model_type"]
    if "evaluations" in value:
        import capo_frauddetector.types.list_of_model_version_evaluations

        out["evaluations"] = (
            capo_frauddetector.types.list_of_model_version_evaluations.serialize_aws_json_1_1(
                value["evaluations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatedModelVersion:
    out: EvaluatedModelVersion = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    if "modelVersion" in data:
        out["model_version"] = data["modelVersion"]
    if "modelType" in data:
        out["model_type"] = data["modelType"]
    if "evaluations" in data:
        import capo_frauddetector.types.list_of_model_version_evaluations

        out["evaluations"] = (
            capo_frauddetector.types.list_of_model_version_evaluations.deserialize_aws_json_1_1(
                data["evaluations"]
            )
        )
    return out
