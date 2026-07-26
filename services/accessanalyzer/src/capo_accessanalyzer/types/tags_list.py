"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#TagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.tags_map

TagsList: TypeAlias = list["capo_accessanalyzer.types.tags_map.TagsMap"]


# --- restJson1 ser/de ---
def serialize_json(value: TagsList) -> list:
    import capo_accessanalyzer.types.tags_map

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.tags_map.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagsList:
    import capo_accessanalyzer.types.tags_map

    out: TagsList = []
    for item in data:
        out.append(capo_accessanalyzer.types.tags_map.deserialize_json(item))
    return out
