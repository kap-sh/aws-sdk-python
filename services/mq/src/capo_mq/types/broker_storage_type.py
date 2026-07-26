"""Generated from Smithy shape ``com.amazonaws.mq#BrokerStorageType``."""

from typing import Literal, TypeAlias, cast

"""<p>The broker's storage type.</p> <important><p>EFS is not supported for RabbitMQ engine type.</p></important>"""
BrokerStorageType: TypeAlias = Literal[
    "EBS",
    "EFS",
]


# --- restJson1 ser/de ---
def serialize_json(value: BrokerStorageType) -> str:
    return value


def deserialize_json(data: str) -> BrokerStorageType:
    return cast(BrokerStorageType, data)
