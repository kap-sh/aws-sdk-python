"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayApplianceModifyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

NatGatewayApplianceModifyState: TypeAlias = Literal[
    "modifying",
    "completed",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: NatGatewayApplianceModifyState) -> str:
    return value


def from_ec2_query_text(text: str) -> NatGatewayApplianceModifyState:
    return cast(NatGatewayApplianceModifyState, text)


def serialize_ec2_query(
    value: NatGatewayApplianceModifyState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NatGatewayApplianceModifyState:
    return from_ec2_query_text(el.text or "")
