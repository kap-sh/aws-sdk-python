"""Generated from Smithy shape ``com.amazonaws.ec2#AssociationTypeEnum``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AssociationTypeEnum: TypeAlias = Literal[
    "tag",
    "instance-id",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AssociationTypeEnum) -> str:
    return value


def from_ec2_query_text(text: str) -> AssociationTypeEnum:
    return cast(AssociationTypeEnum, text)


def serialize_ec2_query(
    value: AssociationTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AssociationTypeEnum:
    return from_ec2_query_text(el.text or "")
