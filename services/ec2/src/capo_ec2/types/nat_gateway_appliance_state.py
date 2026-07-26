"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayApplianceState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

NatGatewayApplianceState: TypeAlias = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
    "attach-failed",
    "detach-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: NatGatewayApplianceState) -> str:
    return value


def from_ec2_query_text(text: str) -> NatGatewayApplianceState:
    return cast(NatGatewayApplianceState, text)


def serialize_ec2_query(
    value: NatGatewayApplianceState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NatGatewayApplianceState:
    return from_ec2_query_text(el.text or "")
