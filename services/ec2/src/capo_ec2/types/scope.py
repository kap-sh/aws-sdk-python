"""Generated from Smithy shape ``com.amazonaws.ec2#scope``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

scope: TypeAlias = Literal[
    "Availability Zone",
    "Region",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: scope) -> str:
    return value


def from_ec2_query_text(text: str) -> scope:
    return cast(scope, text)


def serialize_ec2_query(
    value: scope, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> scope:
    return from_ec2_query_text(el.text or "")
