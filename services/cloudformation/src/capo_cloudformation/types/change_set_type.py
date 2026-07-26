"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ChangeSetType: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "IMPORT",
]


# --- awsQuery ser/de ---
def to_query_text(value: ChangeSetType) -> str:
    return value


def from_query_text(text: str) -> ChangeSetType:
    return cast(ChangeSetType, text)


def serialize_query(
    value: ChangeSetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ChangeSetType:
    return from_query_text(el.text or "")
