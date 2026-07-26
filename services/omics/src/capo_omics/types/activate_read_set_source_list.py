"""Generated from Smithy shape ``com.amazonaws.omics#ActivateReadSetSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.activate_read_set_source_item

ActivateReadSetSourceList: TypeAlias = list[
    "capo_omics.types.activate_read_set_source_item.ActivateReadSetSourceItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActivateReadSetSourceList) -> list:
    import capo_omics.types.activate_read_set_source_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.activate_read_set_source_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActivateReadSetSourceList:
    import capo_omics.types.activate_read_set_source_item

    out: ActivateReadSetSourceList = []
    for item in data:
        out.append(
            capo_omics.types.activate_read_set_source_item.deserialize_json(item)
        )
    return out
