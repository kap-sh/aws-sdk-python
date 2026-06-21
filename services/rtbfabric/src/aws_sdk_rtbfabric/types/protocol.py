"""Generated from Smithy shape ``com.amazonaws.rtbfabric#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal[
    "HTTP",
    "HTTPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    return cast(Protocol, data)
