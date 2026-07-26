"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.export_read_set_detail

ExportReadSetDetailList: TypeAlias = list[
    "capo_omics.types.export_read_set_detail.ExportReadSetDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetDetailList) -> list:
    import capo_omics.types.export_read_set_detail

    out: list = []
    for item in value:
        out.append(capo_omics.types.export_read_set_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportReadSetDetailList:
    import capo_omics.types.export_read_set_detail

    out: ExportReadSetDetailList = []
    for item in data:
        out.append(capo_omics.types.export_read_set_detail.deserialize_json(item))
    return out
