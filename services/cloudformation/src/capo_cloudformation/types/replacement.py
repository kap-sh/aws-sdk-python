"""Generated from Smithy shape ``com.amazonaws.cloudformation#Replacement``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

Replacement: TypeAlias = Literal[
    "True",
    "False",
    "Conditional",
]


# --- awsQuery ser/de ---
def to_query_text(value: Replacement) -> str:
    return value


def from_query_text(text: str) -> Replacement:
    return cast(Replacement, text)


def serialize_query(
    value: Replacement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Replacement:
    return from_query_text(el.text or "")
