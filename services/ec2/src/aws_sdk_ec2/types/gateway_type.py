"""Generated from Smithy shape ``com.amazonaws.ec2#GatewayType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

GatewayType: TypeAlias = Literal["ipsec.1",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: GatewayType) -> str:
    return value


def from_ec2_query_text(text: str) -> GatewayType:
    return cast(GatewayType, text)


def serialize_ec2_query(
    value: GatewayType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> GatewayType:
    return from_ec2_query_text(el.text or "")
