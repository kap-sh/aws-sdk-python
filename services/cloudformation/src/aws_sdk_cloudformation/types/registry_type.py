"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegistryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

RegistryType: TypeAlias = Literal[
    "RESOURCE",
    "MODULE",
    "HOOK",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE",
        "MODULE",
        "HOOK",
    )
)


def to_query_text(value: RegistryType) -> str:
    return value


def from_query_text(text: str) -> RegistryType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RegistryType value: {text!r}")
    return cast(RegistryType, text)


def serialize_query(
    value: RegistryType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RegistryType:
    return from_query_text(el.text or "")
