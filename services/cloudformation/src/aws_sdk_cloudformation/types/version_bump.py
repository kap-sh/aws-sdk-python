"""Generated from Smithy shape ``com.amazonaws.cloudformation#VersionBump``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

VersionBump: TypeAlias = Literal[
    "MAJOR",
    "MINOR",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAJOR",
        "MINOR",
    )
)


def to_query_text(value: VersionBump) -> str:
    return value


def from_query_text(text: str) -> VersionBump:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VersionBump value: {text!r}")
    return cast(VersionBump, text)


def serialize_query(
    value: VersionBump, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> VersionBump:
    return from_query_text(el.text or "")
