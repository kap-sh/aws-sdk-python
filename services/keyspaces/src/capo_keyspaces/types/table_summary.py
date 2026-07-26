"""Generated from Smithy shape ``com.amazonaws.keyspaces#TableSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.table_name


class TableSummary(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace that the table is stored in.</p>"""
    table_name: "capo_keyspaces.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    resource_arn: "capo_keyspaces.types.arn.ARN"
    """<p>The unique identifier of the table in the format of an Amazon Resource Name (ARN).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableSummary) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TableSummary:
    out: TableSummary = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("TableSummary.keyspace_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("TableSummary.table_name required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("TableSummary.resource_arn required")
    return out
