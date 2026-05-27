"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateGlobalTableInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_list
    import aws_sdk_dynamodb.types.table_name


class CreateGlobalTableInput(TypedDict):
    global_table_name: "aws_sdk_dynamodb.types.table_name.TableName"
    """<p>The global table name.</p>"""
    replication_group: "aws_sdk_dynamodb.types.replica_list.ReplicaList"
    """<p>The Regions where the global table needs to be created.</p>"""
