"""Generated from Smithy shape ``com.amazonaws.iam#ReportFormatType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

ReportFormatType: TypeAlias = Literal["text/csv",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("text/csv",))


def to_query_text(value: ReportFormatType) -> str:
    return value


def from_query_text(text: str) -> ReportFormatType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ReportFormatType value: {text!r}")
    return cast(ReportFormatType, text)


def serialize_query(
    value: ReportFormatType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReportFormatType:
    return from_query_text(el.text or "")
