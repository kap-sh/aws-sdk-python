"""Generated from Smithy shape ``com.amazonaws.iam#jobStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

jobStatusType: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def to_query_text(value: jobStatusType) -> str:
    return value


def from_query_text(text: str) -> jobStatusType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown jobStatusType value: {text!r}")
    return cast(jobStatusType, text)


def serialize_query(
    value: jobStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> jobStatusType:
    return from_query_text(el.text or "")
