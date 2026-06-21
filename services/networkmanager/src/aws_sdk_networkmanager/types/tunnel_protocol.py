"""Generated from Smithy shape ``com.amazonaws.networkmanager#TunnelProtocol``."""

from typing import Literal, TypeAlias, cast

TunnelProtocol: TypeAlias = Literal[
    "GRE",
    "NO_ENCAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: TunnelProtocol) -> str:
    return value


def deserialize_json(data: str) -> TunnelProtocol:
    return cast(TunnelProtocol, data)
