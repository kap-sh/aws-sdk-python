"""Generated from Smithy shape ``com.amazonaws.iam#summaryStateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

summaryStateType: TypeAlias = Literal[
    "AVAILABLE",
    "NOT_AVAILABLE",
    "NOT_SUPPORTED",
    "FAILED",
]


# --- awsQuery ser/de ---
def to_query_text(value: summaryStateType) -> str:
    return value


def from_query_text(text: str) -> summaryStateType:
    return cast(summaryStateType, text)


def serialize_query(
    value: summaryStateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> summaryStateType:
    return from_query_text(el.text or "")
