"""Generated from Smithy shape ``com.amazonaws.iam#policyScopeType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

policyScopeType: TypeAlias = Literal[
    "All",
    "AWS",
    "Local",
]


# --- awsQuery ser/de ---
def to_query_text(value: policyScopeType) -> str:
    return value


def from_query_text(text: str) -> policyScopeType:
    return cast(policyScopeType, text)


def serialize_query(
    value: policyScopeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> policyScopeType:
    return from_query_text(el.text or "")
