"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.global_table_arn_string
    import aws_sdk_dynamodb.types.global_table_status
    import aws_sdk_dynamodb.types.replica_description_list
    import aws_sdk_dynamodb.types.table_name


class GlobalTableDescription(TypedDict):
    replication_group: NotRequired[
        "aws_sdk_dynamodb.types.replica_description_list.ReplicaDescriptionList"
    ]
    """<p>The Regions where the global table has replicas.</p>"""
    global_table_arn: NotRequired[
        "aws_sdk_dynamodb.types.global_table_arn_string.GlobalTableArnString"
    ]
    """<p>The unique identifier of the global table.</p>"""
    creation_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>The creation time of the global table.</p>"""
    global_table_status: NotRequired[
        "aws_sdk_dynamodb.types.global_table_status.GlobalTableStatus"
    ]
    """<p>The current state of the global table:</p> <ul> <li> <p> <code>CREATING</code> - The global table is being created.</p> </li> <li> <p> <code>UPDATING</code> - The global table is being updated.</p> </li> <li> <p> <code>DELETING</code> - The global table is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The global table is ready for use.</p> </li> </ul>"""
    global_table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The global table name.</p>"""
