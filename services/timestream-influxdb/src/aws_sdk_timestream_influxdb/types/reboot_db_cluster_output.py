"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#RebootDbClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.cluster_status


class RebootDbClusterOutput(TypedDict, closed=True):
    db_cluster_status: NotRequired[
        "aws_sdk_timestream_influxdb.types.cluster_status.ClusterStatus"
    ]
    """<p>The status of the DB Cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RebootDbClusterOutput) -> dict:
    out: dict = {}
    if "db_cluster_status" in value:
        import aws_sdk_timestream_influxdb.types.cluster_status

        out["dbClusterStatus"] = (
            aws_sdk_timestream_influxdb.types.cluster_status.serialize_aws_json_1_0(
                value["db_cluster_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RebootDbClusterOutput:
    out: RebootDbClusterOutput = {}  # type: ignore[typeddict-item]
    if "dbClusterStatus" in data:
        import aws_sdk_timestream_influxdb.types.cluster_status

        out["db_cluster_status"] = (
            aws_sdk_timestream_influxdb.types.cluster_status.deserialize_aws_json_1_0(
                data["dbClusterStatus"]
            )
        )
    return out
