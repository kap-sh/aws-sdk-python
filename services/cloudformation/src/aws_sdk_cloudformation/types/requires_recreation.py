"""Generated from Smithy shape ``com.amazonaws.cloudformation#RequiresRecreation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

RequiresRecreation: TypeAlias = Literal[
    "Never",
    "Conditionally",
    "Always",
]


# --- awsQuery ser/de ---
def to_query_text(value: RequiresRecreation) -> str:
    return value


def from_query_text(text: str) -> RequiresRecreation:
    return cast(RequiresRecreation, text)


def serialize_query(
    value: RequiresRecreation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RequiresRecreation:
    return from_query_text(el.text or "")
