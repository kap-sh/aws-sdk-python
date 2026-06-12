"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobAbortCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.io_t_job_abort_criteria

IoTJobAbortCriteriaList: TypeAlias = list[
    "aws_sdk_greengrassv2.types.io_t_job_abort_criteria.IoTJobAbortCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobAbortCriteriaList) -> list:
    import aws_sdk_greengrassv2.types.io_t_job_abort_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_greengrassv2.types.io_t_job_abort_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IoTJobAbortCriteriaList:
    import aws_sdk_greengrassv2.types.io_t_job_abort_criteria

    out: IoTJobAbortCriteriaList = []
    for item in data:
        out.append(
            aws_sdk_greengrassv2.types.io_t_job_abort_criteria.deserialize_json(item)
        )
    return out
