"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePartnerAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.partner_app_arn


class DescribePartnerAppRequest(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.partner_app_arn.PartnerAppArn"]
    """<p>The ARN of the SageMaker Partner AI App to describe.</p>"""
    include_available_upgrade: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>When set to <code>TRUE</code>, the response includes available upgrade information for the SageMaker Partner AI App. Default is <code>FALSE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePartnerAppRequest) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "include_available_upgrade" in value:
        out["IncludeAvailableUpgrade"] = value["include_available_upgrade"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePartnerAppRequest:
    out: DescribePartnerAppRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "IncludeAvailableUpgrade" in data:
        out["include_available_upgrade"] = data["IncludeAvailableUpgrade"]
    return out
