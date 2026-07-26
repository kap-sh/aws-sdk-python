"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#IpAddressType``."""

from typing import Literal, TypeAlias, cast

"""<p>The IP address types that can invoke your API or domain name.</p>"""
IpAddressType: TypeAlias = Literal[
    "ipv4",
    "dualstack",
]


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressType) -> str:
    return value


def deserialize_json(data: str) -> IpAddressType:
    return cast(IpAddressType, data)
