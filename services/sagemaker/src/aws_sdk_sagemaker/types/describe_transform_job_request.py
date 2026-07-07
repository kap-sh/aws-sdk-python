"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeTransformJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.transform_job_name


class DescribeTransformJobRequest(TypedDict, closed=True):
    transform_job_name: NotRequired[
        "aws_sdk_sagemaker.types.transform_job_name.TransformJobName"
    ]
    """<p>The name of the transform job that you want to view details of.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTransformJobRequest) -> dict:
    out: dict = {}
    if "transform_job_name" in value:
        out["TransformJobName"] = value["transform_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTransformJobRequest:
    out: DescribeTransformJobRequest = {}  # type: ignore[typeddict-item]
    if "TransformJobName" in data:
        out["transform_job_name"] = data["TransformJobName"]
    return out
