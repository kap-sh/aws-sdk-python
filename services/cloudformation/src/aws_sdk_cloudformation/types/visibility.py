"""Generated from Smithy shape ``com.amazonaws.cloudformation#Visibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

Visibility: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- awsQuery ser/de ---
def to_query_text(value: Visibility) -> str:
    return value


def from_query_text(text: str) -> Visibility:
    return cast(Visibility, text)


def serialize_query(
    value: Visibility, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Visibility:
    return from_query_text(el.text or "")
