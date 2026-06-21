"""Generated from Smithy shape ``com.amazonaws.kafka#ClientBroker``."""

from typing import Literal, TypeAlias, cast

"""<p>Client-broker encryption in transit setting.</p>"""
ClientBroker: TypeAlias = Literal[
    "TLS",
    "TLS_PLAINTEXT",
    "PLAINTEXT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientBroker) -> str:
    return value


def deserialize_json(data: str) -> ClientBroker:
    return cast(ClientBroker, data)
