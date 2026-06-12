"""Generated from Smithy shape ``com.amazonaws.cloudformation#Capability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

Capability: TypeAlias = Literal[
    "CAPABILITY_IAM",
    "CAPABILITY_NAMED_IAM",
    "CAPABILITY_AUTO_EXPAND",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CAPABILITY_IAM",
        "CAPABILITY_NAMED_IAM",
        "CAPABILITY_AUTO_EXPAND",
    )
)


def to_query_text(value: Capability) -> str:
    return value


def from_query_text(text: str) -> Capability:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Capability value: {text!r}")
    return cast(Capability, text)


def serialize_query(
    value: Capability, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Capability:
    return from_query_text(el.text or "")
