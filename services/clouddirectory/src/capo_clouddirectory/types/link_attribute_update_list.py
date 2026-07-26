"""Generated from Smithy shape ``com.amazonaws.clouddirectory#LinkAttributeUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.link_attribute_update

LinkAttributeUpdateList: TypeAlias = list[
    "capo_clouddirectory.types.link_attribute_update.LinkAttributeUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkAttributeUpdateList) -> list:
    import capo_clouddirectory.types.link_attribute_update

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.link_attribute_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinkAttributeUpdateList:
    import capo_clouddirectory.types.link_attribute_update

    out: LinkAttributeUpdateList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.link_attribute_update.deserialize_json(item)
        )
    return out
