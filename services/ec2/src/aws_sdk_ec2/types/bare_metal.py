"""Generated from Smithy shape ``com.amazonaws.ec2#BareMetal``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

BareMetal: TypeAlias = Literal[
    "included",
    "required",
    "excluded",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "included",
        "required",
        "excluded",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "included",
        "required",
        "excluded",
    )
)


def to_ec2_query_text(value: BareMetal) -> str:
    return value


def from_ec2_query_text(text: str) -> BareMetal:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BareMetal value: {text!r}")
    return cast(BareMetal, text)


def serialize_ec2_query(
    value: BareMetal, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> BareMetal:
    return from_ec2_query_text(el.text or "")
