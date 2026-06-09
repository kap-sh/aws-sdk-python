"""Generated from Smithy shape ``com.amazonaws.ec2#VpnTunnelProvisioningStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

VpnTunnelProvisioningStatus: TypeAlias = Literal[
    "available",
    "pending",
    "failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "pending",
        "failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "pending",
        "failed",
    )
)


def to_ec2_query_text(value: VpnTunnelProvisioningStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> VpnTunnelProvisioningStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown VpnTunnelProvisioningStatus value: {text!r}"
        )
    return cast(VpnTunnelProvisioningStatus, text)


def serialize_ec2_query(
    value: VpnTunnelProvisioningStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpnTunnelProvisioningStatus:
    return from_ec2_query_text(el.text or "")
