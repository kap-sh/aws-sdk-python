"""Generated from Smithy shape ``com.amazonaws.mq#__listOfBrokerEngineType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mq.types.broker_engine_type

__listOfBrokerEngineType: TypeAlias = list[
    "capo_mq.types.broker_engine_type.BrokerEngineType"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBrokerEngineType) -> list:
    import capo_mq.types.broker_engine_type

    out: list = []
    for item in value:
        out.append(capo_mq.types.broker_engine_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBrokerEngineType:
    import capo_mq.types.broker_engine_type

    out: __listOfBrokerEngineType = []
    for item in data:
        out.append(capo_mq.types.broker_engine_type.deserialize_json(item))
    return out
