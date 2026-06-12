"""Generated from Smithy shape ``com.amazonaws.iotdataplane#GetRetainedMessageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.payload
    import aws_sdk_iot_data_plane.types.qos
    import aws_sdk_iot_data_plane.types.timestamp
    import aws_sdk_iot_data_plane.types.topic
    import aws_sdk_iot_data_plane.types.user_properties_blob


class GetRetainedMessageResponse(TypedDict):
    topic: NotRequired["aws_sdk_iot_data_plane.types.topic.Topic"]
    """<p>The topic name to which the retained message was published.</p>"""
    payload: NotRequired["aws_sdk_iot_data_plane.types.payload.Payload"]
    """<p>The Base64-encoded message payload of the retained message body.</p>"""
    qos: "aws_sdk_iot_data_plane.types.qos.Qos"
    """<p>The quality of service (QoS) level used to publish the retained message.</p>"""
    last_modified_time: "aws_sdk_iot_data_plane.types.timestamp.Timestamp"
    """<p>The Epoch date and time, in milliseconds, when the retained message was stored by IoT.</p>"""
    user_properties: NotRequired[
        "aws_sdk_iot_data_plane.types.user_properties_blob.UserPropertiesBlob"
    ]
    """<p>A base64-encoded JSON string that includes an array of JSON objects, or null if the retained message doesn't include any user properties.</p> <p>The following example <code>userProperties</code> parameter is a JSON string that represents two user properties. Note that it will be base64-encoded:</p> <p> <code>[{\"deviceName\": \"alpha\"}, {\"deviceCnt\": \"45\"}]</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetainedMessageResponse) -> dict:
    out: dict = {}
    if "topic" in value:
        out["topic"] = value["topic"]
    if "payload" in value:
        import aws_sdk_iot_data_plane.types.payload

        out["payload"] = aws_sdk_iot_data_plane.types.payload.serialize_json(
            value["payload"]
        )
    out["qos"] = value.get("qos", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    if "user_properties" in value:
        import aws_sdk_iot_data_plane.types.user_properties_blob

        out["userProperties"] = (
            aws_sdk_iot_data_plane.types.user_properties_blob.serialize_json(
                value["user_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRetainedMessageResponse:
    out: GetRetainedMessageResponse = {}  # type: ignore[typeddict-item]
    if "topic" in data:
        out["topic"] = data["topic"]
    if "payload" in data:
        import aws_sdk_iot_data_plane.types.payload

        out["payload"] = aws_sdk_iot_data_plane.types.payload.deserialize_json(
            data["payload"]
        )
    if "qos" in data:
        out["qos"] = data["qos"]
    else:
        out["qos"] = 0
    if "lastModifiedTime" in data:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if "userProperties" in data:
        import aws_sdk_iot_data_plane.types.user_properties_blob

        out["user_properties"] = (
            aws_sdk_iot_data_plane.types.user_properties_blob.deserialize_json(
                data["userProperties"]
            )
        )
    return out
