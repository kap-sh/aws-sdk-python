"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceDriftStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

StackResourceDriftStatus: TypeAlias = Literal[
    "IN_SYNC",
    "MODIFIED",
    "DELETED",
    "NOT_CHECKED",
    "UNKNOWN",
    "UNSUPPORTED",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackResourceDriftStatus) -> str:
    return value


def from_query_text(text: str) -> StackResourceDriftStatus:
    return cast(StackResourceDriftStatus, text)


def serialize_query(
    value: StackResourceDriftStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackResourceDriftStatus:
    return from_query_text(el.text or "")
