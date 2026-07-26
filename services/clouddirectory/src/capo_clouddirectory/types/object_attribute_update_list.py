"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectAttributeUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.object_attribute_update

ObjectAttributeUpdateList: TypeAlias = list[
    "capo_clouddirectory.types.object_attribute_update.ObjectAttributeUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: ObjectAttributeUpdateList) -> list:
    import capo_clouddirectory.types.object_attribute_update

    out: list = []
    for item in value:
        out.append(
            capo_clouddirectory.types.object_attribute_update.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ObjectAttributeUpdateList:
    import capo_clouddirectory.types.object_attribute_update

    out: ObjectAttributeUpdateList = []
    for item in data:
        out.append(
            capo_clouddirectory.types.object_attribute_update.deserialize_json(item)
        )
    return out
