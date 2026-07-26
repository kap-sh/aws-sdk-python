"""Generated from Smithy shape ``com.amazonaws.guardduty#ItemPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.item_path

ItemPaths: TypeAlias = list["capo_guardduty.types.item_path.ItemPath"]


# --- restJson1 ser/de ---
def serialize_json(value: ItemPaths) -> list:
    import capo_guardduty.types.item_path

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.item_path.serialize_json(item))
    return out


def deserialize_json(data: list) -> ItemPaths:
    import capo_guardduty.types.item_path

    out: ItemPaths = []
    for item in data:
        out.append(capo_guardduty.types.item_path.deserialize_json(item))
    return out
