"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetJobDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.export_read_set_job_detail

ExportReadSetJobDetailList: TypeAlias = list[
    "capo_omics.types.export_read_set_job_detail.ExportReadSetJobDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetJobDetailList) -> list:
    import capo_omics.types.export_read_set_job_detail

    out: list = []
    for item in value:
        out.append(capo_omics.types.export_read_set_job_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportReadSetJobDetailList:
    import capo_omics.types.export_read_set_job_detail

    out: ExportReadSetJobDetailList = []
    for item in data:
        out.append(capo_omics.types.export_read_set_job_detail.deserialize_json(item))
    return out
