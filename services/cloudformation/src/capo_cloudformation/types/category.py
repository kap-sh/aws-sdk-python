"""Generated from Smithy shape ``com.amazonaws.cloudformation#Category``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

Category: TypeAlias = Literal[
    "REGISTERED",
    "ACTIVATED",
    "THIRD_PARTY",
    "AWS_TYPES",
]


# --- awsQuery ser/de ---
def to_query_text(value: Category) -> str:
    return value


def from_query_text(text: str) -> Category:
    return cast(Category, text)


def serialize_query(value: Category, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Category:
    return from_query_text(el.text or "")
