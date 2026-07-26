"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListResourcesAssociatedToCustomLineItemFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_relationship


class ListResourcesAssociatedToCustomLineItemFilter(TypedDict, closed=True):
    relationship: NotRequired[
        "capo_billingconductor.types.custom_line_item_relationship.CustomLineItemRelationship"
    ]
    """<p> The type of relationship between the custom line item and the associated resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesAssociatedToCustomLineItemFilter) -> dict:
    out: dict = {}
    if "relationship" in value:
        import capo_billingconductor.types.custom_line_item_relationship

        out["Relationship"] = (
            capo_billingconductor.types.custom_line_item_relationship.serialize_json(
                value["relationship"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListResourcesAssociatedToCustomLineItemFilter:
    out: ListResourcesAssociatedToCustomLineItemFilter = {}  # type: ignore[typeddict-item]
    if "Relationship" in data:
        import capo_billingconductor.types.custom_line_item_relationship

        out["relationship"] = (
            capo_billingconductor.types.custom_line_item_relationship.deserialize_json(
                data["Relationship"]
            )
        )
    return out
