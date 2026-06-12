"""Generated from Smithy shape ``com.amazonaws.mq#__listOfBrokerInstance``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.broker_instance

__listOfBrokerInstance: TypeAlias = list[
    "aws_sdk_mq.types.broker_instance.BrokerInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBrokerInstance) -> list:
    import aws_sdk_mq.types.broker_instance

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.broker_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBrokerInstance:
    import aws_sdk_mq.types.broker_instance

    out: __listOfBrokerInstance = []
    for item in data:
        out.append(aws_sdk_mq.types.broker_instance.deserialize_json(item))
    return out
