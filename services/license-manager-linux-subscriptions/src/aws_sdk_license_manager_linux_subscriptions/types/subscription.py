"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.box_long


class Subscription(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the subscription.</p>"""
    type: NotRequired["str"]
    """<p>The type of subscription. The type can be subscription-included with Amazon EC2, Bring Your Own Subscription model (BYOS), or from the Amazon Web Services Marketplace. Certain subscriptions may use licensing from the Amazon Web Services Marketplace as well as OS licensing from Amazon EC2 or BYOS.</p>"""
    instance_count: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.box_long.BoxLong"
    ]
    """<p>The total amount of running instances using this subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Subscription) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    return out


def deserialize_json(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    return out
