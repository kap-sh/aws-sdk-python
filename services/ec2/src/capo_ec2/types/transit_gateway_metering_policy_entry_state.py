"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyEntryState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayMeteringPolicyEntryState: TypeAlias = Literal[
    "available",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayMeteringPolicyEntryState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayMeteringPolicyEntryState:
    return cast(TransitGatewayMeteringPolicyEntryState, text)


def serialize_ec2_query(
    value: TransitGatewayMeteringPolicyEntryState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayMeteringPolicyEntryState:
    return from_ec2_query_text(el.text or "")
