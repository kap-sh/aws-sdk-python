"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ChangeSource: TypeAlias = Literal[
    "ResourceReference",
    "ParameterReference",
    "ResourceAttribute",
    "DirectModification",
    "Automatic",
    "NoModification",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResourceReference",
        "ParameterReference",
        "ResourceAttribute",
        "DirectModification",
        "Automatic",
        "NoModification",
    )
)


def to_query_text(value: ChangeSource) -> str:
    return value


def from_query_text(text: str) -> ChangeSource:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ChangeSource value: {text!r}")
    return cast(ChangeSource, text)


def serialize_query(
    value: ChangeSource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ChangeSource:
    return from_query_text(el.text or "")
