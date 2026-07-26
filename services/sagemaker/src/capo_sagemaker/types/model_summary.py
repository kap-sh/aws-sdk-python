"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_arn
    import capo_sagemaker.types.model_name
    import capo_sagemaker.types.timestamp


class ModelSummary(TypedDict, closed=True):
    model_name: NotRequired["capo_sagemaker.types.model_name.ModelName"]
    """<p>The name of the model that you want a summary for.</p>"""
    model_arn: NotRequired["capo_sagemaker.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the model.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the model was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSummary) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelSummary:
    out: ModelSummary = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
