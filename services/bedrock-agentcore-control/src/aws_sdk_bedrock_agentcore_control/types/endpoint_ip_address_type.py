"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EndpointIpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

EndpointIpAddressType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
    )
)


def serialize_json(value: EndpointIpAddressType) -> str:
    return value


def deserialize_json(data: str) -> EndpointIpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointIpAddressType value: {data!r}")
    return cast(EndpointIpAddressType, data)
