"""Generated from Smithy shape ``com.amazonaws.networkmanager#TunnelProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

TunnelProtocol: TypeAlias = Literal[
    "GRE",
    "NO_ENCAP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GRE",
        "NO_ENCAP",
    )
)


def serialize_json(value: TunnelProtocol) -> str:
    return value


def deserialize_json(data: str) -> TunnelProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TunnelProtocol value: {data!r}")
    return cast(TunnelProtocol, data)
