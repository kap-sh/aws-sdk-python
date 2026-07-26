"""Generated from Smithy shape ``com.amazonaws.ec2#AddressFamily``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

AddressFamily: TypeAlias = Literal[
    "ipv4",
    "ipv6",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: AddressFamily) -> str:
    return value


def from_ec2_query_text(text: str) -> AddressFamily:
    return cast(AddressFamily, text)


def serialize_ec2_query(
    value: AddressFamily, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> AddressFamily:
    return from_ec2_query_text(el.text or "")
