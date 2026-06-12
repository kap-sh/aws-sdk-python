"""Generated from Smithy shape ``com.amazonaws.mq#EngineType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>The type of broker engine. Amazon MQ supports ActiveMQ and RabbitMQ.</p>"""
EngineType: TypeAlias = Literal[
    "ACTIVEMQ",
    "RABBITMQ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVEMQ",
        "RABBITMQ",
    )
)


def serialize_json(value: EngineType) -> str:
    return value


def deserialize_json(data: str) -> EngineType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngineType value: {data!r}")
    return cast(EngineType, data)
