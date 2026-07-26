"""Generated from Smithy shape ``com.amazonaws.ec2#ListingStatus``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ListingStatus: TypeAlias = Literal[
    "active",
    "pending",
    "cancelled",
    "closed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ListingStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> ListingStatus:
    return cast(ListingStatus, text)


def serialize_ec2_query(
    value: ListingStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ListingStatus:
    return from_ec2_query_text(el.text or "")
