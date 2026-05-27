"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateGlobalTableInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_update_list
    import aws_sdk_dynamodb.types.table_name


class UpdateGlobalTableInput(TypedDict):
    global_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The global table name.</p>"""
    replica_updates: "aws_sdk_dynamodb.types.replica_update_list.ReplicaUpdateList"
    """<p>A list of Regions that should be added or removed from the global table.</p>"""
