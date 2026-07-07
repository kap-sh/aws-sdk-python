"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeDeploymentModelConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class EdgeDeploymentModelConfig(TypedDict, closed=True):
    model_handle: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name the device application uses to reference this model.</p>"""
    edge_packaging_job_name: NotRequired[
        "aws_sdk_sagemaker.types.entity_name.EntityName"
    ]
    """<p>The edge packaging job associated with this deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeDeploymentModelConfig) -> dict:
    out: dict = {}
    if "model_handle" in value:
        out["ModelHandle"] = value["model_handle"]
    if "edge_packaging_job_name" in value:
        out["EdgePackagingJobName"] = value["edge_packaging_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgeDeploymentModelConfig:
    out: EdgeDeploymentModelConfig = {}  # type: ignore[typeddict-item]
    if "ModelHandle" in data:
        out["model_handle"] = data["ModelHandle"]
    if "EdgePackagingJobName" in data:
        out["edge_packaging_job_name"] = data["EdgePackagingJobName"]
    return out
