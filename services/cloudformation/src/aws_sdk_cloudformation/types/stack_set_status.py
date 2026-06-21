"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

StackSetStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETED",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackSetStatus) -> str:
    return value


def from_query_text(text: str) -> StackSetStatus:
    return cast(StackSetStatus, text)


def serialize_query(
    value: StackSetStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackSetStatus:
    return from_query_text(el.text or "")
