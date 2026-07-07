"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociateResourceResponseElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.associate_resource_error
    import aws_sdk_billingconductor.types.custom_line_item_association_element


class AssociateResourceResponseElement(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_association_element.CustomLineItemAssociationElement"
    ]
    """<p>The resource ARN that was associated to the custom line item.</p>"""
    error: NotRequired[
        "aws_sdk_billingconductor.types.associate_resource_error.AssociateResourceError"
    ]
    """<p>An <code>AssociateResourceError</code> that will populate if the resource association fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceResponseElement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "error" in value:
        import aws_sdk_billingconductor.types.associate_resource_error

        out["Error"] = (
            aws_sdk_billingconductor.types.associate_resource_error.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateResourceResponseElement:
    out: AssociateResourceResponseElement = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Error" in data:
        import aws_sdk_billingconductor.types.associate_resource_error

        out["error"] = (
            aws_sdk_billingconductor.types.associate_resource_error.deserialize_json(
                data["Error"]
            )
        )
    return out
