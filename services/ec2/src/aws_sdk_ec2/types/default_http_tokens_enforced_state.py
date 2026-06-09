"""Generated from Smithy shape ``com.amazonaws.ec2#DefaultHttpTokensEnforcedState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

DefaultHttpTokensEnforcedState: TypeAlias = Literal[
    "disabled",
    "enabled",
    "no-preference",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
        "no-preference",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "disabled",
        "enabled",
        "no-preference",
    )
)


def to_ec2_query_text(value: DefaultHttpTokensEnforcedState) -> str:
    return value


def from_ec2_query_text(text: str) -> DefaultHttpTokensEnforcedState:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown DefaultHttpTokensEnforcedState value: {text!r}"
        )
    return cast(DefaultHttpTokensEnforcedState, text)


def serialize_ec2_query(
    value: DefaultHttpTokensEnforcedState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DefaultHttpTokensEnforcedState:
    return from_ec2_query_text(el.text or "")
