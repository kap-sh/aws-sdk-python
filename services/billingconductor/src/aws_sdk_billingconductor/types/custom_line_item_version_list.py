"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_version_list_element

CustomLineItemVersionList: TypeAlias = list[
    "aws_sdk_billingconductor.types.custom_line_item_version_list_element.CustomLineItemVersionListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemVersionList) -> list:
    import aws_sdk_billingconductor.types.custom_line_item_version_list_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.custom_line_item_version_list_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CustomLineItemVersionList:
    import aws_sdk_billingconductor.types.custom_line_item_version_list_element

    out: CustomLineItemVersionList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.custom_line_item_version_list_element.deserialize_json(
                item
            )
        )
    return out
