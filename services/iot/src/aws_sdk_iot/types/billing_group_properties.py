"""Generated from Smithy shape ``com.amazonaws.iot#BillingGroupProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.billing_group_description


class BillingGroupProperties(TypedDict):
    billing_group_description: NotRequired[
        "aws_sdk_iot.types.billing_group_description.BillingGroupDescription"
    ]
    """<p>The description of the billing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupProperties) -> dict:
    out: dict = {}
    if "billing_group_description" in value:
        out["billingGroupDescription"] = value["billing_group_description"]
    return out


def deserialize_json(data: dict) -> BillingGroupProperties:
    out: BillingGroupProperties = {}  # type: ignore[typeddict-item]
    if "billingGroupDescription" in data:
        out["billing_group_description"] = data["billingGroupDescription"]
    return out
