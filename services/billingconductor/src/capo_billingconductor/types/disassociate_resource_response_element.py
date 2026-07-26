"""Generated from Smithy shape ``com.amazonaws.billingconductor#DisassociateResourceResponseElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.associate_resource_error
    import capo_billingconductor.types.custom_line_item_association_element


class DisassociateResourceResponseElement(TypedDict, closed=True):
    arn: NotRequired[
        "capo_billingconductor.types.custom_line_item_association_element.CustomLineItemAssociationElement"
    ]
    """<p>The resource ARN that was disassociated from the custom line item. </p>"""
    error: NotRequired[
        "capo_billingconductor.types.associate_resource_error.AssociateResourceError"
    ]
    """<p> An <code>AssociateResourceError</code> that's shown if the resource disassociation fails. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceResponseElement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "error" in value:
        import capo_billingconductor.types.associate_resource_error

        out["Error"] = (
            capo_billingconductor.types.associate_resource_error.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateResourceResponseElement:
    out: DisassociateResourceResponseElement = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Error" in data:
        import capo_billingconductor.types.associate_resource_error

        out["error"] = (
            capo_billingconductor.types.associate_resource_error.deserialize_json(
                data["Error"]
            )
        )
    return out
