"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkDirection``."""

from typing import Literal, TypeAlias, cast

NetworkDirection: TypeAlias = Literal[
    "INBOUND",
    "OUTBOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkDirection) -> str:
    return value


def deserialize_json(data: str) -> NetworkDirection:
    return cast(NetworkDirection, data)
