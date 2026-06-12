"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#MqttTopicConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.iam_role_arn
    import aws_sdk_iotfleetwise.types.mqtt_topic_arn


class MqttTopicConfig(TypedDict):
    mqtt_topic_arn: "aws_sdk_iotfleetwise.types.mqtt_topic_arn.MqttTopicArn"
    """<p>The ARN of the MQTT topic.</p>"""
    execution_role_arn: "aws_sdk_iotfleetwise.types.iam_role_arn.IAMRoleArn"
    """<p>The ARN of the role that grants Amazon Web Services IoT FleetWise permission to access and act on messages sent to the MQTT topic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MqttTopicConfig) -> dict:
    out: dict = {}
    out["mqttTopicArn"] = value["mqtt_topic_arn"]
    out["executionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MqttTopicConfig:
    out: MqttTopicConfig = {}  # type: ignore[typeddict-item]
    if "mqttTopicArn" in data:
        out["mqtt_topic_arn"] = data["mqttTopicArn"]
    else:
        raise DeserializationError("MqttTopicConfig.mqtt_topic_arn required")
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("MqttTopicConfig.execution_role_arn required")
    return out
