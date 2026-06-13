"""Generated from Smithy shape ``com.amazonaws.devopsagent#IpAddressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>IP address type for a Resource Gateway.</p>"""
IpAddressType: TypeAlias = Literal[
    "IPV4",
    "IPV6",
    "DUAL_STACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IPV4",
        "IPV6",
        "DUAL_STACK",
    )
)


def serialize_json(value: IpAddressType) -> str:
    return value


def deserialize_json(data: str) -> IpAddressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpAddressType value: {data!r}")
    return cast(IpAddressType, data)
