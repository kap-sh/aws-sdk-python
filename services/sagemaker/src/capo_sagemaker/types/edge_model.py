"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_version
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.timestamp


class EdgeModel(TypedDict, closed=True):
    model_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model.</p>"""
    model_version: NotRequired["capo_sagemaker.types.edge_version.EdgeVersion"]
    """<p>The model version.</p>"""
    latest_sample_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of the last data sample taken.</p>"""
    latest_inference: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The timestamp of the last inference that was made.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeModel) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "latest_sample_time" in value:
        import capo_sagemaker.types.timestamp

        out["LatestSampleTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["latest_sample_time"]
        )
    if "latest_inference" in value:
        import capo_sagemaker.types.timestamp

        out["LatestInference"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["latest_inference"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgeModel:
    out: EdgeModel = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "LatestSampleTime" in data:
        import capo_sagemaker.types.timestamp

        out["latest_sample_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LatestSampleTime"]
            )
        )
    if "LatestInference" in data:
        import capo_sagemaker.types.timestamp

        out["latest_inference"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LatestInference"]
            )
        )
    return out
