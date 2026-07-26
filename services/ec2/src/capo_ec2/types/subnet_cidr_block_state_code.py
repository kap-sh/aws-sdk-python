"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetCidrBlockStateCode``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

SubnetCidrBlockStateCode: TypeAlias = Literal[
    "associating",
    "associated",
    "disassociating",
    "disassociated",
    "failing",
    "failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: SubnetCidrBlockStateCode) -> str:
    return value


def from_ec2_query_text(text: str) -> SubnetCidrBlockStateCode:
    return cast(SubnetCidrBlockStateCode, text)


def serialize_ec2_query(
    value: SubnetCidrBlockStateCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> SubnetCidrBlockStateCode:
    return from_ec2_query_text(el.text or "")
