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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableDescription) -> dict:
    out: dict = {}
    if "replication_group" in value:
        import aws_sdk_dynamodb.types.replica_description_list

        out["ReplicationGroup"] = (
            aws_sdk_dynamodb.types.replica_description_list.serialize_aws_json_1_0(
                value["replication_group"]
            )
        )
    if "global_table_arn" in value:
        out["GlobalTableArn"] = value["global_table_arn"]
    if "creation_date_time" in value:
        import aws_sdk_dynamodb.types.date

        out["CreationDateTime"] = aws_sdk_dynamodb.types.date.serialize_aws_json_1_0(
            value["creation_date_time"]
        )
    if "global_table_status" in value:
        import aws_sdk_dynamodb.types.global_table_status

        out["GlobalTableStatus"] = (
            aws_sdk_dynamodb.types.global_table_status.serialize_aws_json_1_0(
                value["global_table_status"]
            )
        )
    if "global_table_name" in value:
        out["GlobalTableName"] = value["global_table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalTableDescription:
    out: GlobalTableDescription = {}  # type: ignore[typeddict-item]
    if "ReplicationGroup" in data:
        import aws_sdk_dynamodb.types.replica_description_list

        out["replication_group"] = (
            aws_sdk_dynamodb.types.replica_description_list.deserialize_aws_json_1_0(
                data["ReplicationGroup"]
            )
        )
    if "GlobalTableArn" in data:
        out["global_table_arn"] = data["GlobalTableArn"]
    if "CreationDateTime" in data:
        import aws_sdk_dynamodb.types.date

        out["creation_date_time"] = (
            aws_sdk_dynamodb.types.date.deserialize_aws_json_1_0(
                data["CreationDateTime"]
            )
        )
    if "GlobalTableStatus" in data:
        import aws_sdk_dynamodb.types.global_table_status

        out["global_table_status"] = (
            aws_sdk_dynamodb.types.global_table_status.deserialize_aws_json_1_0(
                data["GlobalTableStatus"]
            )
        )
    if "GlobalTableName" in data:
        out["global_table_name"] = data["GlobalTableName"]
    return out
