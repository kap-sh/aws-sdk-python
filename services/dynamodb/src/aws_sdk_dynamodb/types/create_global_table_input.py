"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateGlobalTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_list
    import aws_sdk_dynamodb.types.table_name


class CreateGlobalTableInput(TypedDict, closed=True):
    global_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The global table name.</p>"""
    replication_group: "aws_sdk_dynamodb.types.replica_list.ReplicaList"
    """<p>The Regions where the global table needs to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateGlobalTableInput) -> dict:
    out: dict = {}
    out["GlobalTableName"] = value["global_table_name"]
    import aws_sdk_dynamodb.types.replica_list

    out["ReplicationGroup"] = (
        aws_sdk_dynamodb.types.replica_list.serialize_aws_json_1_0(
            value["replication_group"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateGlobalTableInput:
    out: CreateGlobalTableInput = {}  # type: ignore[typeddict-item]
    if "GlobalTableName" in data:
        out["global_table_name"] = data["GlobalTableName"]
    else:
        raise DeserializationError("CreateGlobalTableInput.global_table_name required")
    if "ReplicationGroup" in data:
        import aws_sdk_dynamodb.types.replica_list

        out["replication_group"] = (
            aws_sdk_dynamodb.types.replica_list.deserialize_aws_json_1_0(
                data["ReplicationGroup"]
            )
        )
    else:
        raise DeserializationError("CreateGlobalTableInput.replication_group required")
    return out
