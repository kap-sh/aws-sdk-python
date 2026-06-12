"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ChangeSetStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "DELETE_PENDING",
    "DELETE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_PENDING",
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "DELETE_PENDING",
        "DELETE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
        "FAILED",
    )
)


def to_query_text(value: ChangeSetStatus) -> str:
    return value


def from_query_text(text: str) -> ChangeSetStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ChangeSetStatus value: {text!r}")
    return cast(ChangeSetStatus, text)


def serialize_query(
    value: ChangeSetStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ChangeSetStatus:
    return from_query_text(el.text or "")
