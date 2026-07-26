"""Generated from Smithy shape ``com.amazonaws.ec2#TokenState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

TokenState: TypeAlias = Literal[
    "valid",
    "expired",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: TokenState) -> str:
    return value


def from_ec2_query_text(text: str) -> TokenState:
    return cast(TokenState, text)


def serialize_ec2_query(
    value: TokenState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TokenState:
    return from_ec2_query_text(el.text or "")
