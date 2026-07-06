"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DeleteDbClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_influxdb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_cluster_id


class DeleteDbClusterInput(TypedDict, closed=True):
    db_cluster_id: "aws_sdk_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDbClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDbClusterInput:
    out: DeleteDbClusterInput = {}  # type: ignore[typeddict-item]
    if "dbClusterId" in data:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        raise DeserializationError("DeleteDbClusterInput.db_cluster_id required")
    return out
