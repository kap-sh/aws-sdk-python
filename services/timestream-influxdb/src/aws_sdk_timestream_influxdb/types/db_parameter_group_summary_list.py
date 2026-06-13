"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbParameterGroupSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_parameter_group_summary

DbParameterGroupSummaryList: TypeAlias = list[
    "aws_sdk_timestream_influxdb.types.db_parameter_group_summary.DbParameterGroupSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbParameterGroupSummaryList) -> list:
    import aws_sdk_timestream_influxdb.types.db_parameter_group_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_timestream_influxdb.types.db_parameter_group_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DbParameterGroupSummaryList:
    import aws_sdk_timestream_influxdb.types.db_parameter_group_summary

    out: DbParameterGroupSummaryList = []
    for item in data:
        out.append(
            aws_sdk_timestream_influxdb.types.db_parameter_group_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
