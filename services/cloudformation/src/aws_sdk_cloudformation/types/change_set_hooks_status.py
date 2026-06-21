"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetHooksStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

ChangeSetHooksStatus: TypeAlias = Literal[
    "PLANNING",
    "PLANNED",
    "UNAVAILABLE",
]


# --- awsQuery ser/de ---
def to_query_text(value: ChangeSetHooksStatus) -> str:
    return value


def from_query_text(text: str) -> ChangeSetHooksStatus:
    return cast(ChangeSetHooksStatus, text)


def serialize_query(
    value: ChangeSetHooksStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ChangeSetHooksStatus:
    return from_query_text(el.text or "")
