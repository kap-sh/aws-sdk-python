"""Generated from Smithy shape ``com.amazonaws.sagemaker#EMRStepMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.string1024


class EMRStepMetadata(TypedDict):
    cluster_id: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The identifier of the EMR cluster.</p>"""
    step_id: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The identifier of the EMR cluster step.</p>"""
    step_name: NotRequired["aws_sdk_sagemaker.types.string256.String256"]
    """<p>The name of the EMR cluster step.</p>"""
    log_file_path: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p>The path to the log file where the cluster step's failure root cause is recorded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EMRStepMetadata) -> dict:
    out: dict = {}
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "step_id" in value:
        out["StepId"] = value["step_id"]
    if "step_name" in value:
        out["StepName"] = value["step_name"]
    if "log_file_path" in value:
        out["LogFilePath"] = value["log_file_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EMRStepMetadata:
    out: EMRStepMetadata = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "StepId" in data:
        out["step_id"] = data["StepId"]
    if "StepName" in data:
        out["step_name"] = data["StepName"]
    if "LogFilePath" in data:
        out["log_file_path"] = data["LogFilePath"]
    return out
