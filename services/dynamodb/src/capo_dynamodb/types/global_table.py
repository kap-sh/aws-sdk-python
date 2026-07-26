"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_list
    import capo_dynamodb.types.table_name


class GlobalTable(TypedDict, closed=True):
    global_table_name: NotRequired["capo_dynamodb.types.table_name.TableName"]
    """<p>The global table name.</p>"""
    replication_group: NotRequired["capo_dynamodb.types.replica_list.ReplicaList"]
    """<p>The Regions where the global table has replicas.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTable) -> dict:
    out: dict = {}
    if "global_table_name" in value:
        out["GlobalTableName"] = value["global_table_name"]
    if "replication_group" in value:
        import capo_dynamodb.types.replica_list

        out["ReplicationGroup"] = (
            capo_dynamodb.types.replica_list.serialize_aws_json_1_0(
                value["replication_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalTable:
    out: GlobalTable = {}  # type: ignore[typeddict-item]
    if "GlobalTableName" in data:
        out["global_table_name"] = data["GlobalTableName"]
    if "ReplicationGroup" in data:
        import capo_dynamodb.types.replica_list

        out["replication_group"] = (
            capo_dynamodb.types.replica_list.deserialize_aws_json_1_0(
                data["ReplicationGroup"]
            )
        )
    return out
