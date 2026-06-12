"""Generated from Smithy shape ``com.amazonaws.iot#MetricsExportConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.mqtt_topic
    import aws_sdk_iot.types.role_arn


class MetricsExportConfig(TypedDict):
    mqtt_topic: "aws_sdk_iot.types.mqtt_topic.MqttTopic"
    """<p>The MQTT topic that Device Defender Detect should publish messages to for metrics export.</p>"""
    role_arn: "aws_sdk_iot.types.role_arn.RoleArn"
    """<p>This role ARN has permission to publish MQTT messages, after which Device Defender Detect can assume the role and publish messages on your behalf.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricsExportConfig) -> dict:
    out: dict = {}
    out["mqttTopic"] = value["mqtt_topic"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> MetricsExportConfig:
    out: MetricsExportConfig = {}  # type: ignore[typeddict-item]
    if "mqttTopic" in data:
        out["mqtt_topic"] = data["mqttTopic"]
    else:
        raise DeserializationError("MetricsExportConfig.mqtt_topic required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("MetricsExportConfig.role_arn required")
    return out
