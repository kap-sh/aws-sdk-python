"""Generated from Smithy shape ``com.amazonaws.omics#ImportReadSetJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.import_read_set_job_item

ImportReadSetJobList: TypeAlias = list[
    "capo_omics.types.import_read_set_job_item.ImportReadSetJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportReadSetJobList) -> list:
    import capo_omics.types.import_read_set_job_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.import_read_set_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportReadSetJobList:
    import capo_omics.types.import_read_set_job_item

    out: ImportReadSetJobList = []
    for item in data:
        out.append(capo_omics.types.import_read_set_job_item.deserialize_json(item))
    return out
