"""Generated from Smithy shape ``com.amazonaws.redshift#TableRestoreStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

TableRestoreStatusType: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "CANCELED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
        "CANCELED",
    )
)


def to_query_text(value: TableRestoreStatusType) -> str:
    return value


def from_query_text(text: str) -> TableRestoreStatusType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TableRestoreStatusType value: {text!r}")
    return cast(TableRestoreStatusType, text)


def serialize_query(
    value: TableRestoreStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TableRestoreStatusType:
    return from_query_text(el.text or "")
