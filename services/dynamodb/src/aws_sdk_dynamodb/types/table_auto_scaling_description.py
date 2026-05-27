"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableAutoScalingDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.replica_auto_scaling_description_list
    import aws_sdk_dynamodb.types.table_name
    import aws_sdk_dynamodb.types.table_status


class TableAutoScalingDescription(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_name.TableName"]
    """<p>The name of the table.</p>"""
    table_status: NotRequired["aws_sdk_dynamodb.types.table_status.TableStatus"]
    """<p>The current state of the table:</p> <ul> <li> <p> <code>CREATING</code> - The table is being created.</p> </li> <li> <p> <code>UPDATING</code> - The table is being updated.</p> </li> <li> <p> <code>DELETING</code> - The table is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The table is ready for use.</p> </li> </ul>"""
    replicas: NotRequired[
        "aws_sdk_dynamodb.types.replica_auto_scaling_description_list.ReplicaAutoScalingDescriptionList"
    ]
    """<p>Represents replicas of the global table.</p>"""
