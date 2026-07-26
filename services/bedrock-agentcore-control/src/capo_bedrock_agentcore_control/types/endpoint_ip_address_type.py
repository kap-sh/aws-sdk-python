"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EndpointIpAddressType``."""

from typing import Literal, TypeAlias, cast

EndpointIpAddressType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointIpAddressType) -> str:
    return value


def deserialize_json(data: str) -> EndpointIpAddressType:
    return cast(EndpointIpAddressType, data)
