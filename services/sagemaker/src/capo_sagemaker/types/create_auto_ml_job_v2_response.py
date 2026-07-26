"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateAutoMLJobV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_arn


class CreateAutoMLJobV2Response(TypedDict, closed=True):
    auto_ml_job_arn: NotRequired["capo_sagemaker.types.auto_ml_job_arn.AutoMLJobArn"]
    """<p>The unique ARN assigned to the AutoMLJob when it is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAutoMLJobV2Response) -> dict:
    out: dict = {}
    if "auto_ml_job_arn" in value:
        out["AutoMLJobArn"] = value["auto_ml_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAutoMLJobV2Response:
    out: CreateAutoMLJobV2Response = {}  # type: ignore[typeddict-item]
    if "AutoMLJobArn" in data:
        out["auto_ml_job_arn"] = data["AutoMLJobArn"]
    return out
