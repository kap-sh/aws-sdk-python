"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbInstanceForClusterSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_instance_for_cluster_summary

DbInstanceForClusterSummaryList: TypeAlias = list[
    "capo_timestream_influxdb.types.db_instance_for_cluster_summary.DbInstanceForClusterSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbInstanceForClusterSummaryList) -> list:
    import capo_timestream_influxdb.types.db_instance_for_cluster_summary

    out: list = []
    for item in value:
        out.append(
            capo_timestream_influxdb.types.db_instance_for_cluster_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DbInstanceForClusterSummaryList:
    import capo_timestream_influxdb.types.db_instance_for_cluster_summary

    out: DbInstanceForClusterSummaryList = []
    for item in data:
        out.append(
            capo_timestream_influxdb.types.db_instance_for_cluster_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
