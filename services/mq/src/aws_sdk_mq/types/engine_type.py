"""Generated from Smithy shape ``com.amazonaws.mq#EngineType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ.</p>"""
EngineType: TypeAlias = Literal[
    "ACTIVEMQ",
    "RABBITMQ",
]


# --- restJson1 ser/de ---
def serialize_json(value: EngineType) -> str:
    return value


def deserialize_json(data: str) -> EngineType:
    return cast(EngineType, data)
