"""Generated from Smithy shape ``com.amazonaws.iot#AddThingToBillingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.billing_group_arn
    import aws_sdk_iot.types.billing_group_name
    import aws_sdk_iot.types.thing_arn
    import aws_sdk_iot.types.thing_name


class AddThingToBillingGroupRequest(TypedDict):
    billing_group_name: NotRequired[
        "aws_sdk_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group.</p> <note> <p>This call is asynchronous. It might take several seconds for the detachment to propagate.</p> </note>"""
    billing_group_arn: NotRequired[
        "aws_sdk_iot.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The ARN of the billing group.</p>"""
    thing_name: NotRequired["aws_sdk_iot.types.thing_name.ThingName"]
    """<p>The name of the thing to be added to the billing group.</p>"""
    thing_arn: NotRequired["aws_sdk_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing to be added to the billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddThingToBillingGroupRequest) -> dict:
    out: dict = {}
    if "billing_group_name" in value:
        out["billingGroupName"] = value["billing_group_name"]
    if "billing_group_arn" in value:
        out["billingGroupArn"] = value["billing_group_arn"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    return out


def deserialize_json(data: dict) -> AddThingToBillingGroupRequest:
    out: AddThingToBillingGroupRequest = {}  # type: ignore[typeddict-item]
    if "billingGroupName" in data:
        out["billing_group_name"] = data["billingGroupName"]
    if "billingGroupArn" in data:
        out["billing_group_arn"] = data["billingGroupArn"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    return out
