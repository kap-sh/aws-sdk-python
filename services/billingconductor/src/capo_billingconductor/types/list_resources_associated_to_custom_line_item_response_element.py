"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListResourcesAssociatedToCustomLineItemResponseElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period
    import capo_billingconductor.types.custom_line_item_association_element
    import capo_billingconductor.types.custom_line_item_relationship


class ListResourcesAssociatedToCustomLineItemResponseElement(TypedDict, closed=True):
    arn: NotRequired[
        "capo_billingconductor.types.custom_line_item_association_element.CustomLineItemAssociationElement"
    ]
    """<p> The ARN of the associated resource. </p>"""
    relationship: NotRequired[
        "capo_billingconductor.types.custom_line_item_relationship.CustomLineItemRelationship"
    ]
    """<p> The type of relationship between the custom line item and the associated resource. </p>"""
    end_billing_period: NotRequired[
        "capo_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The end billing period of the associated resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ListResourcesAssociatedToCustomLineItemResponseElement,
) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "relationship" in value:
        import capo_billingconductor.types.custom_line_item_relationship

        out["Relationship"] = (
            capo_billingconductor.types.custom_line_item_relationship.serialize_json(
                value["relationship"]
            )
        )
    if "end_billing_period" in value:
        out["EndBillingPeriod"] = value["end_billing_period"]
    return out


def deserialize_json(
    data: dict,
) -> ListResourcesAssociatedToCustomLineItemResponseElement:
    out: ListResourcesAssociatedToCustomLineItemResponseElement = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Relationship" in data:
        import capo_billingconductor.types.custom_line_item_relationship

        out["relationship"] = (
            capo_billingconductor.types.custom_line_item_relationship.deserialize_json(
                data["Relationship"]
            )
        )
    if "EndBillingPeriod" in data:
        out["end_billing_period"] = data["EndBillingPeriod"]
    return out
