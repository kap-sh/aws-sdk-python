"""Generated from Smithy shape ``com.amazonaws.ec2#DefaultRouteTableAssociationValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element

DefaultRouteTableAssociationValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: DefaultRouteTableAssociationValue) -> str:
    return value


def from_ec2_query_text(text: str) -> DefaultRouteTableAssociationValue:
    return cast(DefaultRouteTableAssociationValue, text)


def serialize_ec2_query(
    value: DefaultRouteTableAssociationValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DefaultRouteTableAssociationValue:
    return from_ec2_query_text(el.text or "")
