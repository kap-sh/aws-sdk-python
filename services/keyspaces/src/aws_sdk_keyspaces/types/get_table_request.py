"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.table_name


class GetTableRequest(TypedDict, closed=True):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace that the table is stored in.</p>"""
    table_name: "aws_sdk_keyspaces.types.table_name.TableName"
    """<p>The name of the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTableRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTableRequest:
    out: GetTableRequest = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("GetTableRequest.keyspace_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("GetTableRequest.table_name required")
    return out
