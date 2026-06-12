"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeOfferingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ReservedNodeOfferingType: TypeAlias = Literal[
    "Regular",
    "Upgradable",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Regular",
        "Upgradable",
    )
)


def to_query_text(value: ReservedNodeOfferingType) -> str:
    return value


def from_query_text(text: str) -> ReservedNodeOfferingType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReservedNodeOfferingType value: {text!r}")
    return cast(ReservedNodeOfferingType, text)


def serialize_query(
    value: ReservedNodeOfferingType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReservedNodeOfferingType:
    return from_query_text(el.text or "")
