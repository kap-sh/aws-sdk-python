"""Generated from Smithy shape ``com.amazonaws.keyspaces#ReplicationGroupStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.keyspace_status
    import aws_sdk_keyspaces.types.region
    import aws_sdk_keyspaces.types.tables_replication_progress


class ReplicationGroupStatus(TypedDict):
    region: "aws_sdk_keyspaces.types.region.region"
    """<p> The name of the Region that was added to the keyspace. </p>"""
    keyspace_status: "aws_sdk_keyspaces.types.keyspace_status.KeyspaceStatus"
    """<p> The status of the keyspace. </p>"""
    tables_replication_progress: NotRequired[
        "aws_sdk_keyspaces.types.tables_replication_progress.TablesReplicationProgress"
    ]
    """<p> This shows the replication progress of tables in the keyspace. The value is expressed as a percentage of the newly replicated tables with status <code>Active</code> compared to the total number of tables in the keyspace. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReplicationGroupStatus) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    out["keyspaceStatus"] = value["keyspace_status"]
    if "tables_replication_progress" in value:
        out["tablesReplicationProgress"] = value["tables_replication_progress"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReplicationGroupStatus:
    out: ReplicationGroupStatus = {}  # type: ignore[typeddict-item]
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("ReplicationGroupStatus.region required")
    if "keyspaceStatus" in data:
        out["keyspace_status"] = data["keyspaceStatus"]
    else:
        raise DeserializationError("ReplicationGroupStatus.keyspace_status required")
    if "tablesReplicationProgress" in data:
        out["tables_replication_progress"] = data["tablesReplicationProgress"]
    return out
