"""Generated from Smithy shape ``com.amazonaws.iam#DeletionTaskStatusType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

DeletionTaskStatusType: TypeAlias = Literal[
    "SUCCEEDED",
    "IN_PROGRESS",
    "FAILED",
    "NOT_STARTED",
]


# --- awsQuery ser/de ---
def to_query_text(value: DeletionTaskStatusType) -> str:
    return value


def from_query_text(text: str) -> DeletionTaskStatusType:
    return cast(DeletionTaskStatusType, text)


def serialize_query(
    value: DeletionTaskStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DeletionTaskStatusType:
    return from_query_text(el.text or "")
