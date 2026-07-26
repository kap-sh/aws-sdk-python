"""Generated from Smithy shape ``com.amazonaws.iot#RemoveThingFromBillingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.billing_group_arn
    import capo_iot.types.billing_group_name
    import capo_iot.types.thing_arn
    import capo_iot.types.thing_name


class RemoveThingFromBillingGroupRequest(TypedDict, closed=True):
    billing_group_name: NotRequired[
        "capo_iot.types.billing_group_name.BillingGroupName"
    ]
    """<p>The name of the billing group.</p>"""
    billing_group_arn: NotRequired["capo_iot.types.billing_group_arn.BillingGroupArn"]
    """<p>The ARN of the billing group.</p>"""
    thing_name: NotRequired["capo_iot.types.thing_name.ThingName"]
    """<p>The name of the thing to be removed from the billing group.</p>"""
    thing_arn: NotRequired["capo_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing to be removed from the billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveThingFromBillingGroupRequest) -> dict:
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


def deserialize_json(data: dict) -> RemoveThingFromBillingGroupRequest:
    out: RemoveThingFromBillingGroupRequest = {}  # type: ignore[typeddict-item]
    if "billingGroupName" in data:
        out["billing_group_name"] = data["billingGroupName"]
    if "billingGroupArn" in data:
        out["billing_group_arn"] = data["billingGroupArn"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    return out
