"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeAutoMLJobV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_name


class DescribeAutoMLJobV2Request(TypedDict, closed=True):
    auto_ml_job_name: NotRequired["capo_sagemaker.types.auto_ml_job_name.AutoMLJobName"]
    """<p>Requests information about an AutoML job V2 using its unique name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutoMLJobV2Request) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutoMLJobV2Request:
    out: DescribeAutoMLJobV2Request = {}  # type: ignore[typeddict-item]
    if "AutoMLJobName" in data:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    return out
