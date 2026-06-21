"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ProxySessionStatus``."""

from typing import Literal, TypeAlias, cast

ProxySessionStatus: TypeAlias = Literal[
    "Open",
    "InProgress",
    "Closed",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProxySessionStatus) -> str:
    return value


def deserialize_json(data: str) -> ProxySessionStatus:
    return cast(ProxySessionStatus, data)
