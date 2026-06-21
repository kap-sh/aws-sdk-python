"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBfdState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

RouteServerBfdState: TypeAlias = Literal[
    "up",
    "down",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RouteServerBfdState) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerBfdState:
    return cast(RouteServerBfdState, text)


def serialize_ec2_query(
    value: RouteServerBfdState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerBfdState:
    return from_ec2_query_text(el.text or "")
