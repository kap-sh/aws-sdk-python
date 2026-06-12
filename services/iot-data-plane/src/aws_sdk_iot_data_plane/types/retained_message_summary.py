"""Generated from Smithy shape ``com.amazonaws.iotdataplane#RetainedMessageSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.payload_size
    import aws_sdk_iot_data_plane.types.qos
    import aws_sdk_iot_data_plane.types.timestamp
    import aws_sdk_iot_data_plane.types.topic


class RetainedMessageSummary(TypedDict):
    topic: NotRequired["aws_sdk_iot_data_plane.types.topic.Topic"]
    """<p>The topic name to which the retained message was published.</p>"""
    payload_size: "aws_sdk_iot_data_plane.types.payload_size.PayloadSize"
    """<p>The size of the retained message's payload in bytes.</p>"""
    qos: "aws_sdk_iot_data_plane.types.qos.Qos"
    """<p>The quality of service (QoS) level used to publish the retained message.</p>"""
    last_modified_time: "aws_sdk_iot_data_plane.types.timestamp.Timestamp"
    """<p>The Epoch date and time, in milliseconds, when the retained message was stored by IoT.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetainedMessageSummary) -> dict:
    out: dict = {}
    if "topic" in value:
        out["topic"] = value["topic"]
    out["payloadSize"] = value.get("payload_size", 0)
    out["qos"] = value.get("qos", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    return out


def deserialize_json(data: dict) -> RetainedMessageSummary:
    out: RetainedMessageSummary = {}  # type: ignore[typeddict-item]
    if "topic" in data:
        out["topic"] = data["topic"]
    if "payloadSize" in data:
        out["payload_size"] = data["payloadSize"]
    else:
        out["payload_size"] = 0
    if "qos" in data:
        out["qos"] = data["qos"]
    else:
        out["qos"] = 0
    if "lastModifiedTime" in data:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    return out
