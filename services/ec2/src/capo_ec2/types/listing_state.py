"""Generated from Smithy shape ``com.amazonaws.ec2#ListingState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ListingState: TypeAlias = Literal[
    "available",
    "sold",
    "cancelled",
    "pending",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ListingState) -> str:
    return value


def from_ec2_query_text(text: str) -> ListingState:
    return cast(ListingState, text)


def serialize_ec2_query(
    value: ListingState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ListingState:
    return from_ec2_query_text(el.text or "")
