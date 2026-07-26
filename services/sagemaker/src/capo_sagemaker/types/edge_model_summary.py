"""Generated from Smithy shape ``com.amazonaws.sagemaker#EdgeModelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.edge_version
    import capo_sagemaker.types.entity_name


class EdgeModelSummary(TypedDict, closed=True):
    model_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model.</p>"""
    model_version: NotRequired["capo_sagemaker.types.edge_version.EdgeVersion"]
    """<p>The version model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EdgeModelSummary) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EdgeModelSummary:
    out: EdgeModelSummary = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    return out
