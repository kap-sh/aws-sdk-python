"""Generated from Smithy shape ``com.amazonaws.ec2#VpnProtocol``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

VpnProtocol: TypeAlias = Literal["openvpn",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("openvpn",))


_VALUES: frozenset[str] = frozenset(("openvpn",))


def to_ec2_query_text(value: VpnProtocol) -> str:
    return value


def from_ec2_query_text(text: str) -> VpnProtocol:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VpnProtocol value: {text!r}")
    return cast(VpnProtocol, text)


def serialize_ec2_query(
    value: VpnProtocol, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpnProtocol:
    return from_ec2_query_text(el.text or "")
