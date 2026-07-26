"""Generated from Smithy shape ``com.amazonaws.omics#ImportReadSetSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.import_read_set_source_item

ImportReadSetSourceList: TypeAlias = list[
    "capo_omics.types.import_read_set_source_item.ImportReadSetSourceItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportReadSetSourceList) -> list:
    import capo_omics.types.import_read_set_source_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.import_read_set_source_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportReadSetSourceList:
    import capo_omics.types.import_read_set_source_item

    out: ImportReadSetSourceList = []
    for item in data:
        out.append(capo_omics.types.import_read_set_source_item.deserialize_json(item))
    return out
