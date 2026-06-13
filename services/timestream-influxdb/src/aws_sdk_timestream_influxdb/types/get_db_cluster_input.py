"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#GetDbClusterInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_cluster_id


class GetDbClusterInput(TypedDict):
    db_cluster_id: "aws_sdk_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDbClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDbClusterInput:
    out: GetDbClusterInput = {}  # type: ignore[typeddict-item]
    if "dbClusterId" in data:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        raise DeserializationError("GetDbClusterInput.db_cluster_id required")
    return out
