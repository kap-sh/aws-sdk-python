"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableAutoScalingDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.replica_auto_scaling_description_list
    import capo_dynamodb.types.table_name
    import capo_dynamodb.types.table_status


class TableAutoScalingDescription(TypedDict, closed=True):
    table_name: NotRequired["capo_dynamodb.types.table_name.TableName"]
    """<p>The name of the table.</p>"""
    table_status: NotRequired["capo_dynamodb.types.table_status.TableStatus"]
    """<p>The current state of the table:</p> <ul> <li> <p> <code>CREATING</code> - The table is being created.</p> </li> <li> <p> <code>UPDATING</code> - The table is being updated.</p> </li> <li> <p> <code>DELETING</code> - The table is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The table is ready for use.</p> </li> </ul>"""
    replicas: NotRequired[
        "capo_dynamodb.types.replica_auto_scaling_description_list.ReplicaAutoScalingDescriptionList"
    ]
    """<p>Represents replicas of the global table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableAutoScalingDescription) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "table_status" in value:
        import capo_dynamodb.types.table_status

        out["TableStatus"] = capo_dynamodb.types.table_status.serialize_aws_json_1_0(
            value["table_status"]
        )
    if "replicas" in value:
        import capo_dynamodb.types.replica_auto_scaling_description_list

        out["Replicas"] = (
            capo_dynamodb.types.replica_auto_scaling_description_list.serialize_aws_json_1_0(
                value["replicas"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TableAutoScalingDescription:
    out: TableAutoScalingDescription = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "TableStatus" in data:
        import capo_dynamodb.types.table_status

        out["table_status"] = capo_dynamodb.types.table_status.deserialize_aws_json_1_0(
            data["TableStatus"]
        )
    if "Replicas" in data:
        import capo_dynamodb.types.replica_auto_scaling_description_list

        out["replicas"] = (
            capo_dynamodb.types.replica_auto_scaling_description_list.deserialize_aws_json_1_0(
                data["Replicas"]
            )
        )
    return out
