"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobAbortCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_job_abort_criteria

IoTJobAbortCriteriaList: TypeAlias = list[
    "capo_greengrassv2.types.io_t_job_abort_criteria.IoTJobAbortCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobAbortCriteriaList) -> list:
    import capo_greengrassv2.types.io_t_job_abort_criteria

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.io_t_job_abort_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> IoTJobAbortCriteriaList:
    import capo_greengrassv2.types.io_t_job_abort_criteria

    out: IoTJobAbortCriteriaList = []
    for item in data:
        out.append(
            capo_greengrassv2.types.io_t_job_abort_criteria.deserialize_json(item)
        )
    return out
