"""Generated from Smithy shape ``com.amazonaws.mq#__listOfBrokerInstanceOption``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.broker_instance_option

__listOfBrokerInstanceOption: TypeAlias = list[
    "capo_mq.types.broker_instance_option.BrokerInstanceOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBrokerInstanceOption) -> list:
    import capo_mq.types.broker_instance_option

    out: list = []
    for item in value:
        out.append(capo_mq.types.broker_instance_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBrokerInstanceOption:
    import capo_mq.types.broker_instance_option

    out: __listOfBrokerInstanceOption = []
    for item in data:
        out.append(capo_mq.types.broker_instance_option.deserialize_json(item))
    return out
