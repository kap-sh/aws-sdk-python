"""Generated from Smithy shape ``com.amazonaws.cloudformation#PolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

PolicyAction: TypeAlias = Literal[
    "Delete",
    "Retain",
    "Snapshot",
    "ReplaceAndDelete",
    "ReplaceAndRetain",
    "ReplaceAndSnapshot",
]


# --- awsQuery ser/de ---
def to_query_text(value: PolicyAction) -> str:
    return value


def from_query_text(text: str) -> PolicyAction:
    return cast(PolicyAction, text)


def serialize_query(
    value: PolicyAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PolicyAction:
    return from_query_text(el.text or "")
