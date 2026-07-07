"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_arn


class AutoMLJobStepMetadata(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The Amazon Resource Name (ARN) of the AutoML job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobStepMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLJobStepMetadata:
    out: AutoMLJobStepMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
