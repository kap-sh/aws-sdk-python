"""Generated from Smithy shape ``com.amazonaws.ec2#ReplacementStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

ReplacementStrategy: TypeAlias = Literal[
    "launch",
    "launch-before-terminate",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "launch",
        "launch-before-terminate",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "launch",
        "launch-before-terminate",
    )
)


def to_ec2_query_text(value: ReplacementStrategy) -> str:
    return value


def from_ec2_query_text(text: str) -> ReplacementStrategy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReplacementStrategy value: {text!r}")
    return cast(ReplacementStrategy, text)


def serialize_ec2_query(
    value: ReplacementStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> ReplacementStrategy:
    return from_ec2_query_text(el.text or "")
