"""Generated from Smithy shape ``com.amazonaws.redshift#SortByOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

SortByOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def to_query_text(value: SortByOrder) -> str:
    return value


def from_query_text(text: str) -> SortByOrder:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SortByOrder value: {text!r}")
    return cast(SortByOrder, text)


def serialize_query(
    value: SortByOrder, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SortByOrder:
    return from_query_text(el.text or "")
