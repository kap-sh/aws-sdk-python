"""Generated from Smithy shape ``com.amazonaws.iot#KafkaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.client_properties
    import aws_sdk_iot.types.kafka_headers
    import aws_sdk_iot.types.string


class KafkaAction(TypedDict, closed=True):
    destination_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The ARN of Kafka action's VPC <code>TopicRuleDestination</code>.</p>"""
    topic: "aws_sdk_iot.types.string.String"
    """<p>The Kafka topic for messages to be sent to the Kafka broker.</p>"""
    key: NotRequired["aws_sdk_iot.types.string.String"]
    """<p>The Kafka message key.</p>"""
    partition: NotRequired["aws_sdk_iot.types.string.String"]
    """<p>The Kafka message partition.</p>"""
    client_properties: "aws_sdk_iot.types.client_properties.ClientProperties"
    """<p>Properties of the Apache Kafka producer client.</p>"""
    headers: NotRequired["aws_sdk_iot.types.kafka_headers.KafkaHeaders"]
    """<p>The list of Kafka headers that you specify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaAction) -> dict:
    out: dict = {}
    out["destinationArn"] = value["destination_arn"]
    out["topic"] = value["topic"]
    if "key" in value:
        out["key"] = value["key"]
    if "partition" in value:
        out["partition"] = value["partition"]
    import aws_sdk_iot.types.client_properties

    out["clientProperties"] = aws_sdk_iot.types.client_properties.serialize_json(
        value["client_properties"]
    )
    if "headers" in value:
        import aws_sdk_iot.types.kafka_headers

        out["headers"] = aws_sdk_iot.types.kafka_headers.serialize_json(
            value["headers"]
        )
    return out


def deserialize_json(data: dict) -> KafkaAction:
    out: KafkaAction = {}  # type: ignore[typeddict-item]
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    else:
        raise DeserializationError("KafkaAction.destination_arn required")
    if "topic" in data:
        out["topic"] = data["topic"]
    else:
        raise DeserializationError("KafkaAction.topic required")
    if "key" in data:
        out["key"] = data["key"]
    if "partition" in data:
        out["partition"] = data["partition"]
    if "clientProperties" in data:
        import aws_sdk_iot.types.client_properties

        out["client_properties"] = aws_sdk_iot.types.client_properties.deserialize_json(
            data["clientProperties"]
        )
    else:
        raise DeserializationError("KafkaAction.client_properties required")
    if "headers" in data:
        import aws_sdk_iot.types.kafka_headers

        out["headers"] = aws_sdk_iot.types.kafka_headers.deserialize_json(
            data["headers"]
        )
    return out
