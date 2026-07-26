"""Generated from Smithy shape ``com.amazonaws.ec2#State``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

State: TypeAlias = Literal[
    "PendingAcceptance",
    "Pending",
    "Available",
    "Deleting",
    "Deleted",
    "Rejected",
    "Failed",
    "Expired",
    "Partial",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: State) -> str:
    return value


def from_ec2_query_text(text: str) -> State:
    return cast(State, text)


def serialize_ec2_query(
    value: State, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> State:
    return from_ec2_query_text(el.text or "")
