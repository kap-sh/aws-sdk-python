"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.date
    import capo_dynamodb.types.global_table_arn_string
    import capo_dynamodb.types.global_table_status
    import capo_dynamodb.types.replica_description_list
    import capo_dynamodb.types.table_name


class GlobalTableDescription(TypedDict, closed=True):
    replication_group: NotRequired[
        "capo_dynamodb.types.replica_description_list.ReplicaDescriptionList"
    ]
    """<p>The Regions where the global table has replicas.</p>"""
    global_table_arn: NotRequired[
        "capo_dynamodb.types.global_table_arn_string.GlobalTableArnString"
    ]
    """<p>The unique identifier of the global table.</p>"""
    creation_date_time: NotRequired["capo_dynamodb.types.date.Date"]
    """<p>The creation time of the global table.</p>"""
    global_table_status: NotRequired[
        "capo_dynamodb.types.global_table_status.GlobalTableStatus"
    ]
    """<p>The current state of the global table:</p> <ul> <li> <p> <code>CREATING</code> - The global table is being created.</p> </li> <li> <p> <code>UPDATING</code> - The global table is being updated.</p> </li> <li> <p> <code>DELETING</code> - The global table is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The global table is ready for use.</p> </li> </ul>"""
    global_table_name: NotRequired["capo_dynamodb.types.table_name.TableName"]
    """<p>The global table name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalTableDescription) -> dict:
    out: dict = {}
    if "replication_group" in value:
        import capo_dynamodb.types.replica_description_list

        out["ReplicationGroup"] = (
            capo_dynamodb.types.replica_description_list.serialize_aws_json_1_0(
                value["replication_group"]
            )
        )
    if "global_table_arn" in value:
        out["GlobalTableArn"] = value["global_table_arn"]
    if "creation_date_time" in value:
        import capo_dynamodb.types.date

        out["CreationDateTime"] = capo_dynamodb.types.date.serialize_aws_json_1_0(
            value["creation_date_time"]
        )
    if "global_table_status" in value:
        import capo_dynamodb.types.global_table_status

        out["GlobalTableStatus"] = (
            capo_dynamodb.types.global_table_status.serialize_aws_json_1_0(
                value["global_table_status"]
            )
        )
    if "global_table_name" in value:
        out["GlobalTableName"] = value["global_table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GlobalTableDescription:
    out: GlobalTableDescription = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationGroup") is not None:
        import capo_dynamodb.types.replica_description_list

        out["replication_group"] = (
            capo_dynamodb.types.replica_description_list.deserialize_aws_json_1_0(
                data["ReplicationGroup"]
            )
        )
    if data.get("GlobalTableArn") is not None:
        out["global_table_arn"] = data["GlobalTableArn"]
    if data.get("CreationDateTime") is not None:
        import capo_dynamodb.types.date

        out["creation_date_time"] = capo_dynamodb.types.date.deserialize_aws_json_1_0(
            data["CreationDateTime"]
        )
    if data.get("GlobalTableStatus") is not None:
        import capo_dynamodb.types.global_table_status

        out["global_table_status"] = (
            capo_dynamodb.types.global_table_status.deserialize_aws_json_1_0(
                data["GlobalTableStatus"]
            )
        )
    if data.get("GlobalTableName") is not None:
        out["global_table_name"] = data["GlobalTableName"]
    return out
