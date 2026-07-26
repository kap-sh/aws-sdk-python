"""Generated from Smithy shape ``com.amazonaws.omics#ImportReferenceSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.import_reference_source_item

ImportReferenceSourceList: TypeAlias = list[
    "capo_omics.types.import_reference_source_item.ImportReferenceSourceItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportReferenceSourceList) -> list:
    import capo_omics.types.import_reference_source_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.import_reference_source_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportReferenceSourceList:
    import capo_omics.types.import_reference_source_item

    out: ImportReferenceSourceList = []
    for item in data:
        out.append(capo_omics.types.import_reference_source_item.deserialize_json(item))
    return out
