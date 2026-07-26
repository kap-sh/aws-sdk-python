"""Generated from Smithy shape ``com.amazonaws.ec2#AddressAttributeName``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AddressAttributeName: TypeAlias = Literal["domain-name",]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AddressAttributeName) -> str:
    return value


def from_ec2_query_text(text: str) -> AddressAttributeName:
    return cast(AddressAttributeName, text)


def serialize_ec2_query(
    value: AddressAttributeName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AddressAttributeName:
    return from_ec2_query_text(el.text or "")
