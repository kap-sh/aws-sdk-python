"""Generated from Smithy shape ``com.amazonaws.iam#jobStatusType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

jobStatusType: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsQuery ser/de ---
def to_query_text(value: jobStatusType) -> str:
    return value


def from_query_text(text: str) -> jobStatusType:
    return cast(jobStatusType, text)


def serialize_query(
    value: jobStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> jobStatusType:
    return from_query_text(el.text or "")
