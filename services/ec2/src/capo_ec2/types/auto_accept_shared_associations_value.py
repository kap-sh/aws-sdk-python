"""Generated from Smithy shape ``com.amazonaws.ec2#AutoAcceptSharedAssociationsValue``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AutoAcceptSharedAssociationsValue: TypeAlias = Literal[
    "enable",
    "disable",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AutoAcceptSharedAssociationsValue) -> str:
    return value


def from_ec2_query_text(text: str) -> AutoAcceptSharedAssociationsValue:
    return cast(AutoAcceptSharedAssociationsValue, text)


def serialize_ec2_query(
    value: AutoAcceptSharedAssociationsValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AutoAcceptSharedAssociationsValue:
    return from_ec2_query_text(el.text or "")
