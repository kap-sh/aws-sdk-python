"""Generated from Smithy shape ``com.amazonaws.keyspaces#DeleteTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.table_name


class DeleteTableRequest(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace of the to be deleted table.</p>"""
    table_name: "capo_keyspaces.types.table_name.TableName"
    """<p>The name of the table to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTableRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTableRequest:
    out: DeleteTableRequest = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError("DeleteTableRequest.keyspace_name required")
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("DeleteTableRequest.table_name required")
    return out
