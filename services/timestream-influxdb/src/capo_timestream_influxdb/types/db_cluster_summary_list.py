"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbClusterSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_cluster_summary

DbClusterSummaryList: TypeAlias = list[
    "capo_timestream_influxdb.types.db_cluster_summary.DbClusterSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbClusterSummaryList) -> list:
    import capo_timestream_influxdb.types.db_cluster_summary

    out: list = []
    for item in value:
        out.append(
            capo_timestream_influxdb.types.db_cluster_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DbClusterSummaryList:
    import capo_timestream_influxdb.types.db_cluster_summary

    out: DbClusterSummaryList = []
    for item in data:
        out.append(
            capo_timestream_influxdb.types.db_cluster_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
