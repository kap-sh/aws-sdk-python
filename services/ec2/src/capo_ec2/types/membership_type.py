"""Generated from Smithy shape ``com.amazonaws.ec2#MembershipType``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

MembershipType: TypeAlias = Literal[
    "static",
    "igmp",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: MembershipType) -> str:
    return value


def from_ec2_query_text(text: str) -> MembershipType:
    return cast(MembershipType, text)


def serialize_ec2_query(
    value: MembershipType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> MembershipType:
    return from_ec2_query_text(el.text or "")
