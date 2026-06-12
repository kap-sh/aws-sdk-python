"""Generated from Smithy shape ``com.amazonaws.kafka#ClientBroker``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>Client-broker encryption in transit setting.</p>"""
ClientBroker: TypeAlias = Literal[
    "TLS",
    "TLS_PLAINTEXT",
    "PLAINTEXT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TLS",
        "TLS_PLAINTEXT",
        "PLAINTEXT",
    )
)


def serialize_json(value: ClientBroker) -> str:
    return value


def deserialize_json(data: str) -> ClientBroker:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientBroker value: {data!r}")
    return cast(ClientBroker, data)
