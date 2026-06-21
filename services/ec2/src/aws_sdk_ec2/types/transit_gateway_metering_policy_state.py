"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

TransitGatewayMeteringPolicyState: TypeAlias = Literal[
    "available",
    "deleted",
    "pending",
    "modifying",
    "deleting",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayMeteringPolicyState) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayMeteringPolicyState:
    return cast(TransitGatewayMeteringPolicyState, text)


def serialize_ec2_query(
    value: TransitGatewayMeteringPolicyState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayMeteringPolicyState:
    return from_ec2_query_text(el.text or "")
