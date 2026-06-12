"""Generated from Smithy shape ``com.amazonaws.mq#__listOfBrokerInstanceOption``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.broker_instance_option

__listOfBrokerInstanceOption: TypeAlias = list[
    "aws_sdk_mq.types.broker_instance_option.BrokerInstanceOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBrokerInstanceOption) -> list:
    import aws_sdk_mq.types.broker_instance_option

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.broker_instance_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBrokerInstanceOption:
    import aws_sdk_mq.types.broker_instance_option

    out: __listOfBrokerInstanceOption = []
    for item in data:
        out.append(aws_sdk_mq.types.broker_instance_option.deserialize_json(item))
    return out
