"""Generated from Smithy shape ``com.amazonaws.ec2#ManagedResourceDefaultVisibility``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

ManagedResourceDefaultVisibility: TypeAlias = Literal[
    "hidden",
    "visible",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: ManagedResourceDefaultVisibility) -> str:
    return value


def from_ec2_query_text(text: str) -> ManagedResourceDefaultVisibility:
    return cast(ManagedResourceDefaultVisibility, text)


def serialize_ec2_query(
    value: ManagedResourceDefaultVisibility, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ManagedResourceDefaultVisibility:
    return from_ec2_query_text(el.text or "")
