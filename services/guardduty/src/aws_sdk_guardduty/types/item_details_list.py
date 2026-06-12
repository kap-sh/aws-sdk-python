"""Generated from Smithy shape ``com.amazonaws.guardduty#ItemDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.item_details

ItemDetailsList: TypeAlias = list["aws_sdk_guardduty.types.item_details.ItemDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: ItemDetailsList) -> list:
    import aws_sdk_guardduty.types.item_details

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.item_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ItemDetailsList:
    import aws_sdk_guardduty.types.item_details

    out: ItemDetailsList = []
    for item in data:
        out.append(aws_sdk_guardduty.types.item_details.deserialize_json(item))
    return out
