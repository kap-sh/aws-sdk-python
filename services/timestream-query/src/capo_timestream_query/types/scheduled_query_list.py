"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQueryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_query.types.scheduled_query

ScheduledQueryList: TypeAlias = list[
    "capo_timestream_query.types.scheduled_query.ScheduledQuery"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQueryList) -> list:
    import capo_timestream_query.types.scheduled_query

    out: list = []
    for item in value:
        out.append(
            capo_timestream_query.types.scheduled_query.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ScheduledQueryList:
    import capo_timestream_query.types.scheduled_query

    out: ScheduledQueryList = []
    for item in data:
        out.append(
            capo_timestream_query.types.scheduled_query.deserialize_aws_json_1_0(item)
        )
    return out
