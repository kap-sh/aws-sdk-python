"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBgpState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

RouteServerBgpState: TypeAlias = Literal[
    "up",
    "down",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RouteServerBgpState) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerBgpState:
    return cast(RouteServerBgpState, text)


def serialize_ec2_query(
    value: RouteServerBgpState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerBgpState:
    return from_ec2_query_text(el.text or "")
