"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateTransformJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.transform_job_arn


class CreateTransformJobResponse(TypedDict, closed=True):
    transform_job_arn: NotRequired[
        "capo_sagemaker.types.transform_job_arn.TransformJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the transform job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTransformJobResponse) -> dict:
    out: dict = {}
    if "transform_job_arn" in value:
        out["TransformJobArn"] = value["transform_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTransformJobResponse:
    out: CreateTransformJobResponse = {}  # type: ignore[typeddict-item]
    if "TransformJobArn" in data:
        out["transform_job_arn"] = data["TransformJobArn"]
    return out
