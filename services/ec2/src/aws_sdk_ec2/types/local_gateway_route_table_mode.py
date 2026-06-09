"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

LocalGatewayRouteTableMode: TypeAlias = Literal[
    "direct-vpc-routing",
    "coip",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "direct-vpc-routing",
        "coip",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "direct-vpc-routing",
        "coip",
    )
)


def to_ec2_query_text(value: LocalGatewayRouteTableMode) -> str:
    return value


def from_ec2_query_text(text: str) -> LocalGatewayRouteTableMode:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown LocalGatewayRouteTableMode value: {text!r}"
        )
    return cast(LocalGatewayRouteTableMode, text)


def serialize_ec2_query(
    value: LocalGatewayRouteTableMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LocalGatewayRouteTableMode:
    return from_ec2_query_text(el.text or "")
