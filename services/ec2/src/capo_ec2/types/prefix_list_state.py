"""Generated from Smithy shape ``com.amazonaws.ec2#PrefixListState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

PrefixListState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "modify-in-progress",
    "modify-complete",
    "modify-failed",
    "restore-in-progress",
    "restore-complete",
    "restore-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: PrefixListState) -> str:
    return value


def from_ec2_query_text(text: str) -> PrefixListState:
    return cast(PrefixListState, text)


def serialize_ec2_query(
    value: PrefixListState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> PrefixListState:
    return from_ec2_query_text(el.text or "")
