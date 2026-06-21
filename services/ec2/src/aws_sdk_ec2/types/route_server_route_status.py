"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRouteStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

RouteServerRouteStatus: TypeAlias = Literal[
    "in-rib",
    "in-fib",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RouteServerRouteStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerRouteStatus:
    return cast(RouteServerRouteStatus, text)


def serialize_ec2_query(
    value: RouteServerRouteStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerRouteStatus:
    return from_ec2_query_text(el.text or "")
