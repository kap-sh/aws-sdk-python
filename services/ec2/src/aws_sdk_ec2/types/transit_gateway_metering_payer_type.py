"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPayerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TransitGatewayMeteringPayerType: TypeAlias = Literal[
    "source-attachment-owner",
    "destination-attachment-owner",
    "transit-gateway-owner",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "source-attachment-owner",
        "destination-attachment-owner",
        "transit-gateway-owner",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "source-attachment-owner",
        "destination-attachment-owner",
        "transit-gateway-owner",
    )
)


def to_ec2_query_text(value: TransitGatewayMeteringPayerType) -> str:
    return value


def from_ec2_query_text(text: str) -> TransitGatewayMeteringPayerType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown TransitGatewayMeteringPayerType value: {text!r}"
        )
    return cast(TransitGatewayMeteringPayerType, text)


def serialize_ec2_query(
    value: TransitGatewayMeteringPayerType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TransitGatewayMeteringPayerType:
    return from_ec2_query_text(el.text or "")
