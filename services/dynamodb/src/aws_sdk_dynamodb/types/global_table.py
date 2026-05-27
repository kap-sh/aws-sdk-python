"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTable``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_list
    import aws_sdk_dynamodb.types.table_name


class GlobalTable(TypedDict):
    global_table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The global table name.</p>"""
    replication_group: NotRequired["aws_sdk_dynamodb.types.replica_list.ReplicaList"]
    """<p>The Regions where the global table has replicas.</p>"""
