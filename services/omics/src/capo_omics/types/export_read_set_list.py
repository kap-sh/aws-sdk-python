"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.export_read_set

ExportReadSetList: TypeAlias = list["capo_omics.types.export_read_set.ExportReadSet"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetList) -> list:
    import capo_omics.types.export_read_set

    out: list = []
    for item in value:
        out.append(capo_omics.types.export_read_set.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportReadSetList:
    import capo_omics.types.export_read_set

    out: ExportReadSetList = []
    for item in data:
        out.append(capo_omics.types.export_read_set.deserialize_json(item))
    return out
