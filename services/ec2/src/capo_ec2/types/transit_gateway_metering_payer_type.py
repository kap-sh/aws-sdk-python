"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPayerType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TransitGatewayMeteringPayerType: TypeAlias = Literal[
    "source-attachment-owner",
    "destination-attachment-owner",
    "transit-gateway-owner",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TransitGatewayMeteringPayerType) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayMeteringPayerType:
    return cast(TransitGatewayMeteringPayerType, text)


def serialize_ec2_query(
    value: TransitGatewayMeteringPayerType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayMeteringPayerType:
    return from_ec2_query_text(el.text or "")
