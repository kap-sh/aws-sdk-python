"""Generated from Smithy shape ``com.amazonaws.ec2#IngestionStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

IngestionStatus: TypeAlias = Literal[
    "initial-ingestion-in-progress",
    "ingestion-complete",
    "ingestion-failed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "initial-ingestion-in-progress",
        "ingestion-complete",
        "ingestion-failed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "initial-ingestion-in-progress",
        "ingestion-complete",
        "ingestion-failed",
    )
)


def to_ec2_query_text(value: IngestionStatus) -> str:
    return value


def from_ec2_query_text(text: str) -> IngestionStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown IngestionStatus value: {text!r}")
    return cast(IngestionStatus, text)


def serialize_ec2_query(
    value: IngestionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> IngestionStatus:
    return from_ec2_query_text(el.text or "")
