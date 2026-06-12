"""Generated from Smithy shape ``com.amazonaws.mq#BrokerStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>The broker's storage type.</p> <important><p>EFS is not supported for RabbitMQ engine type.</p></important>"""
BrokerStorageType: TypeAlias = Literal[
    "EBS",
    "EFS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EBS",
        "EFS",
    )
)


def serialize_json(value: BrokerStorageType) -> str:
    return value


def deserialize_json(data: str) -> BrokerStorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrokerStorageType value: {data!r}")
    return cast(BrokerStorageType, data)
