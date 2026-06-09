"""Generated from Smithy shape ``com.amazonaws.ec2#RuleAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

RuleAction: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "allow",
        "deny",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "allow",
        "deny",
    )
)


def to_ec2_query_text(value: RuleAction) -> str:
    return value


def from_ec2_query_text(text: str) -> RuleAction:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RuleAction value: {text!r}")
    return cast(RuleAction, text)


def serialize_ec2_query(
    value: RuleAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> RuleAction:
    return from_ec2_query_text(el.text or "")
