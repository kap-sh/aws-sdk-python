"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ItemizedCharge``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.bounded_string
    import aws_sdk_marketplace_agreement.types.resource_id


class ItemizedCharge(TypedDict):
    dimension_key: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The dimension key as specified in the accepted term.</p>"""
    new_quantity: NotRequired["int"]
    """<p>The requested quantity for this dimension.</p>"""
    old_quantity: NotRequired["int"]
    """<p>The existing quantity for this dimension from the source agreement. This value is <code>0</code> for NEW intent.</p>"""
    charge_reference: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The identifier of the expected charge that this itemized charge contributes to.</p>"""
    incremental_charge_amount: NotRequired[
        "aws_sdk_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The total incremental charge amount for this dimension.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemizedCharge) -> dict:
    out: dict = {}
    if "dimension_key" in value:
        out["dimensionKey"] = value["dimension_key"]
    if "new_quantity" in value:
        out["newQuantity"] = value["new_quantity"]
    if "old_quantity" in value:
        out["oldQuantity"] = value["old_quantity"]
    if "charge_reference" in value:
        out["chargeReference"] = value["charge_reference"]
    if "incremental_charge_amount" in value:
        out["incrementalChargeAmount"] = value["incremental_charge_amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ItemizedCharge:
    out: ItemizedCharge = {}  # type: ignore[typeddict-item]
    if "dimensionKey" in data:
        out["dimension_key"] = data["dimensionKey"]
    if "newQuantity" in data:
        out["new_quantity"] = data["newQuantity"]
    if "oldQuantity" in data:
        out["old_quantity"] = data["oldQuantity"]
    if "chargeReference" in data:
        out["charge_reference"] = data["chargeReference"]
    if "incrementalChargeAmount" in data:
        out["incremental_charge_amount"] = data["incrementalChargeAmount"]
    return out
