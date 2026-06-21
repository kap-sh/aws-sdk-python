"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTableState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TransitGatewayPolicyTableState: TypeAlias = Literal[
    "pending",
    "available",
    "deleting",
    "deleted",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayPolicyTableState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayPolicyTableState:
    return cast(TransitGatewayPolicyTableState, text)


def serialize_ec2_query(
    value: TransitGatewayPolicyTableState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayPolicyTableState:
    return from_ec2_query_text(el.text or "")
