"""Generated from Smithy shape ``com.amazonaws.iot#CreateBillingGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.billing_group_arn
    import aws_sdk_iot.types.billing_group_id
    import aws_sdk_iot.types.billing_group_name


class CreateBillingGroupResponse(TypedDict, closed=True):
    billing_group_name: NotRequired[
        "aws_sdk_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name you gave to the billing group.</p>"""
    billing_group_arn: NotRequired[
        "aws_sdk_iot.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The ARN of the billing group.</p>"""
    billing_group_id: NotRequired["aws_sdk_iot.types.billing_group_id.BillingGroupId"]
    """<p>The ID of the billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBillingGroupResponse) -> dict:
    out: dict = {}
    if "billing_group_name" in value:
        out["billingGroupName"] = value["billing_group_name"]
    if "billing_group_arn" in value:
        out["billingGroupArn"] = value["billing_group_arn"]
    if "billing_group_id" in value:
        out["billingGroupId"] = value["billing_group_id"]
    return out


def deserialize_json(data: dict) -> CreateBillingGroupResponse:
    out: CreateBillingGroupResponse = {}  # type: ignore[typeddict-item]
    if "billingGroupName" in data:
        out["billing_group_name"] = data["billingGroupName"]
    if "billingGroupArn" in data:
        out["billing_group_arn"] = data["billingGroupArn"]
    if "billingGroupId" in data:
        out["billing_group_id"] = data["billingGroupId"]
    return out
