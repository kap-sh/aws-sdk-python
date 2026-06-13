"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#RebootDbClusterInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_cluster_id
    import aws_sdk_timestream_influxdb.types.db_instance_id_list


class RebootDbClusterInput(TypedDict):
    db_cluster_id: "aws_sdk_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to reboot.</p>"""
    instance_ids: NotRequired[
        "aws_sdk_timestream_influxdb.types.db_instance_id_list.DbInstanceIdList"
    ]
    """<p>A list of service-generated unique DB Instance Ids belonging to the DB Cluster to reboot.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RebootDbClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
    if "instance_ids" in value:
        import aws_sdk_timestream_influxdb.types.db_instance_id_list

        out["instanceIds"] = (
            aws_sdk_timestream_influxdb.types.db_instance_id_list.serialize_aws_json_1_0(
                value["instance_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RebootDbClusterInput:
    out: RebootDbClusterInput = {}  # type: ignore[typeddict-item]
    if "dbClusterId" in data:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        raise DeserializationError("RebootDbClusterInput.db_cluster_id required")
    if "instanceIds" in data:
        import aws_sdk_timestream_influxdb.types.db_instance_id_list

        out["instance_ids"] = (
            aws_sdk_timestream_influxdb.types.db_instance_id_list.deserialize_aws_json_1_0(
                data["instanceIds"]
            )
        )
    return out
