"""Generated from Smithy shape ``com.amazonaws.ec2#HttpTokensEnforcedState``."""

from typing import Literal, TypeAlias, cast

from capo_ec2._protocol.xml import Element

HttpTokensEnforcedState: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- ec2Query ser/de ---
def to_ec2_query_text(value: HttpTokensEnforcedState) -> str:
    return value


def from_ec2_query_text(text: str) -> HttpTokensEnforcedState:
    return cast(HttpTokensEnforcedState, text)


def serialize_ec2_query(
    value: HttpTokensEnforcedState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> HttpTokensEnforcedState:
    return from_ec2_query_text(el.text or "")
