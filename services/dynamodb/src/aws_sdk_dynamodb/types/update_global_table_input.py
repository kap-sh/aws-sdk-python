"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalTableInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_update_list
    import aws_sdk_dynamodb.types.table_name


class UpdateGlobalTableInput(TypedDict):
    global_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The global table name.</p>"""
    replica_updates: "aws_sdk_dynamodb.types.replica_update_list.ReplicaUpdateList"
    """<p>A list of Regions that should be added or removed from the global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateGlobalTableInput) -> dict:
    out: dict = {}
    out["GlobalTableName"] = value["global_table_name"]
    import aws_sdk_dynamodb.types.replica_update_list

    out["ReplicaUpdates"] = (
        aws_sdk_dynamodb.types.replica_update_list.serialize_aws_json_1_0(
            value["replica_updates"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateGlobalTableInput:
    out: UpdateGlobalTableInput = {}  # type: ignore[typeddict-item]
    if "GlobalTableName" in data:
        out["global_table_name"] = data["GlobalTableName"]
    else:
        raise DeserializationError("UpdateGlobalTableInput.global_table_name required")
    if "ReplicaUpdates" in data:
        import aws_sdk_dynamodb.types.replica_update_list

        out["replica_updates"] = (
            aws_sdk_dynamodb.types.replica_update_list.deserialize_aws_json_1_0(
                data["ReplicaUpdates"]
            )
        )
    else:
        raise DeserializationError("UpdateGlobalTableInput.replica_updates required")
    return out
