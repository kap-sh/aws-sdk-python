"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

StackInstanceStatus: TypeAlias = Literal[
    "CURRENT",
    "OUTDATED",
    "INOPERABLE",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackInstanceStatus) -> str:
    return value


def from_query_text(text: str) -> StackInstanceStatus:
    return cast(StackInstanceStatus, text)


def serialize_query(
    value: StackInstanceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackInstanceStatus:
    return from_query_text(el.text or "")
