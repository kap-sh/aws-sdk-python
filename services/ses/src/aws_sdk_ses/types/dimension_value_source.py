"""Generated from Smithy shape ``com.amazonaws.ses#DimensionValueSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

DimensionValueSource: TypeAlias = Literal[
    "messageTag",
    "emailHeader",
    "linkTag",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "messageTag",
        "emailHeader",
        "linkTag",
    )
)


def to_query_text(value: DimensionValueSource) -> str:
    return value


def from_query_text(text: str) -> DimensionValueSource:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DimensionValueSource value: {text!r}")
    return cast(DimensionValueSource, text)


def serialize_query(
    value: DimensionValueSource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DimensionValueSource:
    return from_query_text(el.text or "")
