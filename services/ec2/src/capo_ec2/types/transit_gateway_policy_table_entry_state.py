"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableEntryState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayPolicyTableEntryState: TypeAlias = Literal[
    "active",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayPolicyTableEntryState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayPolicyTableEntryState:
    return cast(TransitGatewayPolicyTableEntryState, text)


def serialize_ec2_query(
    value: TransitGatewayPolicyTableEntryState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyTableEntryState:
    return from_ec2_query_text(el.text or "")
