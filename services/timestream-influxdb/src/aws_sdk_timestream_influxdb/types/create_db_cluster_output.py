"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#CreateDbClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.cluster_status
    import aws_sdk_timestream_influxdb.types.db_cluster_id


class CreateDbClusterOutput(TypedDict, closed=True):
    db_cluster_id: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_cluster_id.DbClusterId"
    ]
    """<p>A service-generated unique identifier.</p>"""
    db_cluster_status: NotRequired[
        "aws_sdk_timestream_influxdb.types.cluster_status.ClusterStatus"
    ]
    """<p>The status of the DB cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDbClusterOutput) -> dict:
    out: dict = {}
    if "db_cluster_id" in value:
        out["dbClusterId"] = value["db_cluster_id"]
    if "db_cluster_status" in value:
        import aws_sdk_timestream_influxdb.types.cluster_status

        out["dbClusterStatus"] = (
            aws_sdk_timestream_influxdb.types.cluster_status.serialize_aws_json_1_0(
                value["db_cluster_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDbClusterOutput:
    out: CreateDbClusterOutput = {}  # type: ignore[typeddict-item]
    if "dbClusterId" in data:
        out["db_cluster_id"] = data["dbClusterId"]
    if "dbClusterStatus" in data:
        import aws_sdk_timestream_influxdb.types.cluster_status

        out["db_cluster_status"] = (
            aws_sdk_timestream_influxdb.types.cluster_status.deserialize_aws_json_1_0(
                data["dbClusterStatus"]
            )
        )
    return out
