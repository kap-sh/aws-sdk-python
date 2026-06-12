"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopTransformJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.transform_job_name


class StopTransformJobRequest(TypedDict):
    transform_job_name: NotRequired[
        "aws_sdk_sagemaker.types.transform_job_name.TransformJobName"
    ]
    """<p>The name of the batch transform job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopTransformJobRequest) -> dict:
    out: dict = {}
    if "transform_job_name" in value:
        out["TransformJobName"] = value["transform_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopTransformJobRequest:
    out: StopTransformJobRequest = {}  # type: ignore[typeddict-item]
    if "TransformJobName" in data:
        out["transform_job_name"] = data["TransformJobName"]
    return out
