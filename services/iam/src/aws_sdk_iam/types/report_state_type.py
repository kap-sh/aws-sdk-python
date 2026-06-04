"""Generated from Smithy shape ``com.amazonaws.iam#ReportStateType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

ReportStateType: TypeAlias = Literal[
    "STARTED",
    "INPROGRESS",
    "COMPLETE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTED",
        "INPROGRESS",
        "COMPLETE",
    )
)


def to_query_text(value: ReportStateType) -> str:
    return value


def from_query_text(text: str) -> ReportStateType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReportStateType value: {text!r}")
    return cast(ReportStateType, text)


def serialize_query(
    value: ReportStateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReportStateType:
    return from_query_text(el.text or "")
