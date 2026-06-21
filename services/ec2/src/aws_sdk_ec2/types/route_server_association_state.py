"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerAssociationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

RouteServerAssociationState: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: RouteServerAssociationState) -> str:
    return value


def from_ec2_query_text(text: str) -> RouteServerAssociationState:
    return cast(RouteServerAssociationState, text)


def serialize_ec2_query(
    value: RouteServerAssociationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RouteServerAssociationState:
    return from_ec2_query_text(el.text or "")
