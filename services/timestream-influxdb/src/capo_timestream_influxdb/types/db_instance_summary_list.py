"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbInstanceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_instance_summary

DbInstanceSummaryList: TypeAlias = list[
    "capo_timestream_influxdb.types.db_instance_summary.DbInstanceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbInstanceSummaryList) -> list:
    import capo_timestream_influxdb.types.db_instance_summary

    out: list = []
    for item in value:
        out.append(
            capo_timestream_influxdb.types.db_instance_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DbInstanceSummaryList:
    import capo_timestream_influxdb.types.db_instance_summary

    out: DbInstanceSummaryList = []
    for item in data:
        out.append(
            capo_timestream_influxdb.types.db_instance_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
