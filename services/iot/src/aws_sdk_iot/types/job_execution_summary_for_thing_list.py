"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionSummaryForThingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.job_execution_summary_for_thing

JobExecutionSummaryForThingList: TypeAlias = list[
    "aws_sdk_iot.types.job_execution_summary_for_thing.JobExecutionSummaryForThing"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionSummaryForThingList) -> list:
    import aws_sdk_iot.types.job_execution_summary_for_thing

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot.types.job_execution_summary_for_thing.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> JobExecutionSummaryForThingList:
    import aws_sdk_iot.types.job_execution_summary_for_thing

    out: JobExecutionSummaryForThingList = []
    for item in data:
        out.append(
            aws_sdk_iot.types.job_execution_summary_for_thing.deserialize_json(item)
        )
    return out
