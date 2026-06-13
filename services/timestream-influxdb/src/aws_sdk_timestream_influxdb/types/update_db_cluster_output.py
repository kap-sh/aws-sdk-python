"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#UpdateDbClusterOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.cluster_status


class UpdateDbClusterOutput(TypedDict):
    db_cluster_status: NotRequired[
        "aws_sdk_timestream_influxdb.types.cluster_status.ClusterStatus"
    ]
    """<p>The status of the DB cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDbClusterOutput) -> dict:
    out: dict = {}
    if "db_cluster_status" in value:
        import aws_sdk_timestream_influxdb.types.cluster_status

        out["dbClusterStatus"] = (
            aws_sdk_timestream_influxdb.types.cluster_status.serialize_aws_json_1_0(
                value["db_cluster_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDbClusterOutput:
    out: UpdateDbClusterOutput = {}  # type: ignore[typeddict-item]
    if "dbClusterStatus" in data:
        import aws_sdk_timestream_influxdb.types.cluster_status

        out["db_cluster_status"] = (
            aws_sdk_timestream_influxdb.types.cluster_status.deserialize_aws_json_1_0(
                data["dbClusterStatus"]
            )
        )
    return out
