"""Generated from Smithy shape ``com.amazonaws.iam#ReportStateType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

ReportStateType: TypeAlias = Literal[
    "STARTED",
    "INPROGRESS",
    "COMPLETE",
]


# --- awsQuery ser/de ---
def to_query_text(value: ReportStateType) -> str:
    return value


def from_query_text(text: str) -> ReportStateType:
    return cast(ReportStateType, text)


def serialize_query(
    value: ReportStateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReportStateType:
    return from_query_text(el.text or "")
