"""Generated from Smithy shape ``com.amazonaws.cloudformation#ScanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ScanType: TypeAlias = Literal[
    "FULL",
    "PARTIAL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FULL",
        "PARTIAL",
    )
)


def to_query_text(value: ScanType) -> str:
    return value


def from_query_text(text: str) -> ScanType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ScanType value: {text!r}")
    return cast(ScanType, text)


def serialize_query(value: ScanType, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScanType:
    return from_query_text(el.text or "")
