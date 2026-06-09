"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

LocalGatewayRouteType: TypeAlias = Literal[
    "static",
    "propagated",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "static",
        "propagated",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "static",
        "propagated",
    )
)


def to_ec2_query_text(value: LocalGatewayRouteType) -> str:
    return value


def from_ec2_query_text(text: str) -> LocalGatewayRouteType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LocalGatewayRouteType value: {text!r}")
    return cast(LocalGatewayRouteType, text)


def serialize_ec2_query(
    value: LocalGatewayRouteType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> LocalGatewayRouteType:
    return from_ec2_query_text(el.text or "")
