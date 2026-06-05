"""Generated from Smithy shape ``com.amazonaws.ec2#EnaSupport``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

EnaSupport: TypeAlias = Literal[
    "unsupported",
    "supported",
    "required",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unsupported",
        "supported",
        "required",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "unsupported",
        "supported",
        "required",
    )
)


def to_ec2_query_text(value: EnaSupport) -> str:
    return value


def from_ec2_query_text(text: str) -> EnaSupport:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EnaSupport value: {text!r}")
    return cast(EnaSupport, text)


def serialize_ec2_query(
    value: EnaSupport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> EnaSupport:
    return from_ec2_query_text(el.text or "")
