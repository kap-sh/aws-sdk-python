"""Generated from Smithy shape ``com.amazonaws.iam#ReportContentType``."""

from typing import TypeAlias
from aws_sdk_iam._protocol.xml import Element
import base64

ReportContentType: TypeAlias = bytes


# --- awsQuery ser/de ---
def to_query_text(value: ReportContentType) -> str:
    return base64.b64encode(value).decode("ascii")


def from_query_text(text: str) -> ReportContentType:
    return base64.b64decode(text)


def serialize_query(
    value: ReportContentType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReportContentType:
    return from_query_text(el.text or "")
