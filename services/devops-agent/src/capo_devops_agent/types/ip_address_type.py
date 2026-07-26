"""Generated from Smithy shape ``com.amazonaws.devopsagent#IpAddressType``."""

from typing import Literal, TypeAlias, cast

"""<p>IP address type for a Resource Gateway.</p>"""
IpAddressType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
    "DUAL_STACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressType) -> str:
    return value


def deserialize_json(data: str) -> IpAddressType:
    return cast(IpAddressType, data)
