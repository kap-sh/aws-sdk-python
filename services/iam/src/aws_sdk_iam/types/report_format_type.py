"""Generated from Smithy shape ``com.amazonaws.iam#ReportFormatType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

ReportFormatType: TypeAlias = Literal["text/csv",]


# --- awsQuery ser/de ---
def to_query_text(value: ReportFormatType) -> str:
    return value


def from_query_text(text: str) -> ReportFormatType:
    return cast(ReportFormatType, text)


def serialize_query(
    value: ReportFormatType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReportFormatType:
    return from_query_text(el.text or "")
