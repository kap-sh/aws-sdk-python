"""Generated from Smithy shape ``com.amazonaws.ec2#RouteState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

RouteState: TypeAlias = Literal[
    "active",
    "blackhole",
    "filtered",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RouteState) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteState:
    return cast(RouteState, text)


def serialize_ec2_query(
    value: RouteState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteState:
    return from_ec2_query_text(el.text or "")
