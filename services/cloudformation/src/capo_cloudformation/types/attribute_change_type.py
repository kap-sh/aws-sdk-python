"""Generated from Smithy shape ``com.amazonaws.cloudformation#AttributeChangeType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

AttributeChangeType: TypeAlias = Literal[
    "Add",
    "Remove",
    "Modify",
    "SyncWithActual",
]


# --- awsQuery ser/de ---
def to_query_text(value: AttributeChangeType) -> str:
    return value


def from_query_text(text: str) -> AttributeChangeType:
    return cast(AttributeChangeType, text)


def serialize_query(
    value: AttributeChangeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AttributeChangeType:
    return from_query_text(el.text or "")
