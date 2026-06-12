"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopAutoMLJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_name


class StopAutoMLJobRequest(TypedDict):
    auto_ml_job_name: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_name.AutoMLJobName"
    ]
    """<p>The name of the object you are requesting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAutoMLJobRequest) -> dict:
    out: dict = {}
    if "auto_ml_job_name" in value:
        out["AutoMLJobName"] = value["auto_ml_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAutoMLJobRequest:
    out: StopAutoMLJobRequest = {}  # type: ignore[typeddict-item]
    if "AutoMLJobName" in data:
        out["auto_ml_job_name"] = data["AutoMLJobName"]
    return out
