"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListResourcesAssociatedToCustomLineItemResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_response_element

ListResourcesAssociatedToCustomLineItemResponseList: TypeAlias = list[
    "aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_response_element.ListResourcesAssociatedToCustomLineItemResponseElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListResourcesAssociatedToCustomLineItemResponseList) -> list:
    import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_response_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_response_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListResourcesAssociatedToCustomLineItemResponseList:
    import aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_response_element

    out: ListResourcesAssociatedToCustomLineItemResponseList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.list_resources_associated_to_custom_line_item_response_element.deserialize_json(
                item
            )
        )
    return out
