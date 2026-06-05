"""Generated from Smithy shape ``com.amazonaws.ec2#FindingsFound``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

FindingsFound: TypeAlias = Literal[
    "true",
    "false",
    "unknown",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "true",
        "false",
        "unknown",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "true",
        "false",
        "unknown",
    )
)


def to_ec2_query_text(value: FindingsFound) -> str:
    return value


def from_ec2_query_text(text: str) -> FindingsFound:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FindingsFound value: {text!r}")
    return cast(FindingsFound, text)


def serialize_ec2_query(
    value: FindingsFound, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> FindingsFound:
    return from_ec2_query_text(el.text or "")
