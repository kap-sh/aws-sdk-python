"""Generated from Smithy shape ``com.amazonaws.iotevents#DynamoDBv2Action``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.dynamo_table_name
    import aws_sdk_iot_events.types.payload


class DynamoDBv2Action(TypedDict):
    table_name: "aws_sdk_iot_events.types.dynamo_table_name.DynamoTableName"
    """<p>The name of the DynamoDB table.</p>"""
    payload: NotRequired["aws_sdk_iot_events.types.payload.Payload"]


# --- restJson1 ser/de ---
def serialize_json(value: DynamoDBv2Action) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    if "payload" in value:
        import aws_sdk_iot_events.types.payload

        out["payload"] = aws_sdk_iot_events.types.payload.serialize_json(
            value["payload"]
        )
    return out


def deserialize_json(data: dict) -> DynamoDBv2Action:
    out: DynamoDBv2Action = {}  # type: ignore[typeddict-item]
    if "tableName" in data:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("DynamoDBv2Action.table_name required")
    if "payload" in data:
        import aws_sdk_iot_events.types.payload

        out["payload"] = aws_sdk_iot_events.types.payload.deserialize_json(
            data["payload"]
        )
    return out
