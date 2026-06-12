"""Generated from Smithy shape ``com.amazonaws.cloudformation#RegionConcurrencyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

RegionConcurrencyType: TypeAlias = Literal[
    "SEQUENTIAL",
    "PARALLEL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEQUENTIAL",
        "PARALLEL",
    )
)


def to_query_text(value: RegionConcurrencyType) -> str:
    return value


def from_query_text(text: str) -> RegionConcurrencyType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RegionConcurrencyType value: {text!r}")
    return cast(RegionConcurrencyType, text)


def serialize_query(
    value: RegionConcurrencyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RegionConcurrencyType:
    return from_query_text(el.text or "")
