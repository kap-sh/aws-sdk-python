"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTableAutoScalingSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.keyspace_name
    import aws_sdk_keyspaces.types.table_name


class GetTableAutoScalingSettingsRequest(TypedDict):
    keyspace_name: "aws_sdk_keyspaces.types.keyspace_name.KeyspaceName"
    """<p>The name of the keyspace.</p>"""
    table_name: "aws_sdk_keyspaces.types.table_name.TableName"
    """<p>The name of the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTableAutoScalingSettingsRequest) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["tableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTableAutoScalingSettingsRequest:
    out: GetTableAutoScalingSettingsRequest = {}  # type: ignore[typeddict-item]
    if "keyspaceName" in data:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        raise DeserializationError(
            "GetTableAutoScalingSettingsRequest.keyspace_name required"
        )
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError(
            "GetTableAutoScalingSettingsRequest.table_name required"
        )
    return out
