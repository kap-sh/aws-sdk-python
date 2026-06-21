"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPrefixListReferenceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TransitGatewayPrefixListReferenceState: TypeAlias = Literal[
    "pending",
    "available",
    "modifying",
    "deleting",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayPrefixListReferenceState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayPrefixListReferenceState:
    return cast(TransitGatewayPrefixListReferenceState, text)


def serialize_ec2_query(
    value: TransitGatewayPrefixListReferenceState,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayPrefixListReferenceState:
    return from_ec2_query_text(el.text or "")
