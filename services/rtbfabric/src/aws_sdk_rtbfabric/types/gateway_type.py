"""Generated from Smithy shape ``com.amazonaws.rtbfabric#GatewayType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

"""<p>The type of gateway.</p>"""
GatewayType: TypeAlias = Literal[
    "EXTERNAL",
    "INTERNAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXTERNAL",
        "INTERNAL",
    )
)


def serialize_json(value: GatewayType) -> str:
    return value


def deserialize_json(data: str) -> GatewayType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayType value: {data!r}")
    return cast(GatewayType, data)
