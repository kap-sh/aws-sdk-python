"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceDetailedStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

StackInstanceDetailedStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLED",
    "INOPERABLE",
    "SKIPPED_SUSPENDED_ACCOUNT",
    "FAILED_IMPORT",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackInstanceDetailedStatus) -> str:
    return value


def from_query_text(text: str) -> StackInstanceDetailedStatus:
    return cast(StackInstanceDetailedStatus, text)


def serialize_query(
    value: StackInstanceDetailedStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackInstanceDetailedStatus:
    return from_query_text(el.text or "")
