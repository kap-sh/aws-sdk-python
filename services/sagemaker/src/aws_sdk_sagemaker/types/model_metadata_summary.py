"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelMetadataSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string


class ModelMetadataSummary(TypedDict):
    domain: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The machine learning domain of the model.</p>"""
    framework: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The machine learning framework of the model.</p>"""
    task: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The machine learning task of the model.</p>"""
    model: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name of the model.</p>"""
    framework_version: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The framework version of the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelMetadataSummary) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "framework" in value:
        out["Framework"] = value["framework"]
    if "task" in value:
        out["Task"] = value["task"]
    if "model" in value:
        out["Model"] = value["model"]
    if "framework_version" in value:
        out["FrameworkVersion"] = value["framework_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelMetadataSummary:
    out: ModelMetadataSummary = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Framework" in data:
        out["framework"] = data["Framework"]
    if "Task" in data:
        out["task"] = data["Task"]
    if "Model" in data:
        out["model"] = data["Model"]
    if "FrameworkVersion" in data:
        out["framework_version"] = data["FrameworkVersion"]
    return out
