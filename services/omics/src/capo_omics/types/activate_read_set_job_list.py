"""Generated from Smithy shape ``com.amazonaws.omics#ActivateReadSetJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.activate_read_set_job_item

ActivateReadSetJobList: TypeAlias = list[
    "capo_omics.types.activate_read_set_job_item.ActivateReadSetJobItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActivateReadSetJobList) -> list:
    import capo_omics.types.activate_read_set_job_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.activate_read_set_job_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActivateReadSetJobList:
    import capo_omics.types.activate_read_set_job_item

    out: ActivateReadSetJobList = []
    for item in data:
        out.append(capo_omics.types.activate_read_set_job_item.deserialize_json(item))
    return out
