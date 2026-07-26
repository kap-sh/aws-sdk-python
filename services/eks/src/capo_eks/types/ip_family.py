"""Generated from Smithy shape ``com.amazonaws.eks#IpFamily``."""

from typing import Literal, TypeAlias, cast

IpFamily: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- restJson1 ser/de ---
def serialize_json(value: IpFamily) -> str:
    return value


def deserialize_json(data: str) -> IpFamily:
    return cast(IpFamily, data)
