"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

VpcEndpointType: TypeAlias = Literal[
    "Interface",
    "Gateway",
    "GatewayLoadBalancer",
    "Resource",
    "ServiceNetwork",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: VpcEndpointType) -> str:
    return value


def from_ec2_query_text(text: str) -> VpcEndpointType:
    return cast(VpcEndpointType, text)


def serialize_ec2_query(
    value: VpcEndpointType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> VpcEndpointType:
    return from_ec2_query_text(el.text or "")
