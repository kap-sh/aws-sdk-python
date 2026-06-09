"""Generated from Smithy shape ``com.amazonaws.iam#assignmentStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

assignmentStatusType: TypeAlias = Literal[
    "Assigned",
    "Unassigned",
    "Any",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Assigned",
        "Unassigned",
        "Any",
    )
)


def to_query_text(value: assignmentStatusType) -> str:
    return value


def from_query_text(text: str) -> assignmentStatusType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown assignmentStatusType value: {text!r}")
    return cast(assignmentStatusType, text)


def serialize_query(
    value: assignmentStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> assignmentStatusType:
    return from_query_text(el.text or "")
