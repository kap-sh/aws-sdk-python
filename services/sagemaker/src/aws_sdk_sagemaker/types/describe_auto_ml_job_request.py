"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAutoMLJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_name


class DescribeAutoMLJobRequest(TypedDict, closed=True):
    auto_ml_job_name: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_name.AutoMLJobName"
    ]
    """<p>Requests information about an AutoML job using its unique name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutoMLJobRequest) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutoMLJobRequest:
    out: DescribeAutoMLJobRequest = {}  # type: ignore[typeddict-item]
    if "AutoMLJobName" in data:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    return out
