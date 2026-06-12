"""Generated from Smithy shape ``com.amazonaws.guardduty#ItemPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.item_path

ItemPaths: TypeAlias = list["aws_sdk_guardduty.types.item_path.ItemPath"]


# --- restJson1 ser/de ---
def serialize_json(value: ItemPaths) -> list:
    import aws_sdk_guardduty.types.item_path

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.item_path.serialize_json(item))
    return out


def deserialize_json(data: list) -> ItemPaths:
    import aws_sdk_guardduty.types.item_path

    out: ItemPaths = []
    for item in data:
        out.append(aws_sdk_guardduty.types.item_path.deserialize_json(item))
    return out
