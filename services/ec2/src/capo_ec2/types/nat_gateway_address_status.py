"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAddressStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

NatGatewayAddressStatus: TypeAlias = Literal[
    "assigning",
    "unassigning",
    "associating",
    "disassociating",
    "succeeded",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: NatGatewayAddressStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> NatGatewayAddressStatus:
    return cast(NatGatewayAddressStatus, text)


def serialize_ec2_query(
    value: NatGatewayAddressStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NatGatewayAddressStatus:
    return from_ec2_query_text(el.text or "")
