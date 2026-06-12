"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeExchangeStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ReservedNodeExchangeStatusType: TypeAlias = Literal[
    "REQUESTED",
    "PENDING",
    "IN_PROGRESS",
    "RETRYING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTED",
        "PENDING",
        "IN_PROGRESS",
        "RETRYING",
        "SUCCEEDED",
        "FAILED",
    )
)


def to_query_text(value: ReservedNodeExchangeStatusType) -> str:
    return value


def from_query_text(text: str) -> ReservedNodeExchangeStatusType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown ReservedNodeExchangeStatusType value: {text!r}"
        )
    return cast(ReservedNodeExchangeStatusType, text)


def serialize_query(
    value: ReservedNodeExchangeStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReservedNodeExchangeStatusType:
    return from_query_text(el.text or "")
