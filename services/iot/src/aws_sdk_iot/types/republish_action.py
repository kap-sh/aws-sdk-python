"""Generated from Smithy shape ``com.amazonaws.iot#RepublishAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.mqtt_headers
    import aws_sdk_iot.types.qos
    import aws_sdk_iot.types.topic_pattern


class RepublishAction(TypedDict, closed=True):
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access.</p>"""
    topic: "aws_sdk_iot.types.topic_pattern.TopicPattern"
    """<p>The name of the MQTT topic.</p>"""
    qos: NotRequired["aws_sdk_iot.types.qos.Qos"]
    """<p>The Quality of Service (QoS) level to use when republishing messages. The default value is 0.</p>"""
    headers: NotRequired["aws_sdk_iot.types.mqtt_headers.MqttHeaders"]
    r"""<p>MQTT Version 5.0 headers information. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html\"> MQTT</a> from the Amazon Web Services IoT Core Developer Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepublishAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["topic"] = value["topic"]
    if "qos" in value:
        out["qos"] = value["qos"]
    if "headers" in value:
        import aws_sdk_iot.types.mqtt_headers

        out["headers"] = aws_sdk_iot.types.mqtt_headers.serialize_json(value["headers"])
    return out


def deserialize_json(data: dict) -> RepublishAction:
    out: RepublishAction = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("RepublishAction.role_arn required")
    if "topic" in data:
        out["topic"] = data["topic"]
    else:
        raise DeserializationError("RepublishAction.topic required")
    if "qos" in data:
        out["qos"] = data["qos"]
    if "headers" in data:
        import aws_sdk_iot.types.mqtt_headers

        out["headers"] = aws_sdk_iot.types.mqtt_headers.deserialize_json(
            data["headers"]
        )
    return out
