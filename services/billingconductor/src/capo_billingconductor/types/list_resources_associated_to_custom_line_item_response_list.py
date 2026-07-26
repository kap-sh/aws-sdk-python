"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListResourcesAssociatedToCustomLineItemResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_element

ListResourcesAssociatedToCustomLineItemResponseList: TypeAlias = list[
    "capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_element.ListResourcesAssociatedToCustomLineItemResponseElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesAssociatedToCustomLineItemResponseList) -> list:
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_element

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListResourcesAssociatedToCustomLineItemResponseList:
    import capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_element

    out: ListResourcesAssociatedToCustomLineItemResponseList = []
    for item in data:
        out.append(
            capo_billingconductor.types.list_resources_associated_to_custom_line_item_response_element.deserialize_json(
                item
            )
        )
    return out
