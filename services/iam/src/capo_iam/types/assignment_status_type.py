"""Generated from Smithy shape ``com.amazonaws.iam#assignmentStatusType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

assignmentStatusType: TypeAlias = Literal[
    "Assigned",
    "Unassigned",
    "Any",
]


# --- awsQuery ser/de ---
def to_query_text(value: assignmentStatusType) -> str:
    return value


def from_query_text(text: str) -> assignmentStatusType:
    return cast(assignmentStatusType, text)


def serialize_query(
    value: assignmentStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> assignmentStatusType:
    return from_query_text(el.text or "")
