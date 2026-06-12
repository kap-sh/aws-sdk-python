"""Generated from Smithy shape ``com.amazonaws.sagemaker#TransformJobStepMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.transform_job_arn


class TransformJobStepMetadata(TypedDict):
    arn: NotRequired["aws_sdk_sagemaker.types.transform_job_arn.TransformJobArn"]
    """<p>The Amazon Resource Name (ARN) of the transform job that was run by this step execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformJobStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformJobStepMetadata:
    out: TransformJobStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
