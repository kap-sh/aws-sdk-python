"""Generated from Smithy shape ``com.amazonaws.ec2#HttpTokensEnforcedState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

HttpTokensEnforcedState: TypeAlias = Literal[
    "disabled",
    "enabled",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
    )
)


def to_ec2_query_text(value: HttpTokensEnforcedState) -> str:
    return value


def from_ec2_query_text(text: str) -> HttpTokensEnforcedState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HttpTokensEnforcedState value: {text!r}")
    return cast(HttpTokensEnforcedState, text)


def serialize_ec2_query(
    value: HttpTokensEnforcedState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> HttpTokensEnforcedState:
    return from_ec2_query_text(el.text or "")
