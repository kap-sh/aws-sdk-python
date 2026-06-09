"""Generated from Smithy shape ``com.amazonaws.ec2#TokenState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

TokenState: TypeAlias = Literal[
    "valid",
    "expired",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "valid",
        "expired",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "valid",
        "expired",
    )
)


def to_ec2_query_text(value: TokenState) -> str:
    return value


def from_ec2_query_text(text: str) -> TokenState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TokenState value: {text!r}")
    return cast(TokenState, text)


def serialize_ec2_query(
    value: TokenState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> TokenState:
    return from_ec2_query_text(el.text or "")
