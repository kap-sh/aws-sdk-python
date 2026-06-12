"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeWorkforceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workforce_name


class DescribeWorkforceRequest(TypedDict):
    workforce_name: NotRequired["aws_sdk_sagemaker.types.workforce_name.WorkforceName"]
    """<p>The name of the private workforce whose access you want to restrict. <code>WorkforceName</code> is automatically set to <code>default</code> when a workforce is created and cannot be modified. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkforceRequest) -> dict:
    out: dict = {}
    if "workforce_name" in value:
        out["WorkforceName"] = value["workforce_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkforceRequest:
    out: DescribeWorkforceRequest = {}  # type: ignore[typeddict-item]
    if "WorkforceName" in data:
        out["workforce_name"] = data["WorkforceName"]
    return out
