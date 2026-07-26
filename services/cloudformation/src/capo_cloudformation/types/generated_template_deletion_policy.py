"""Generated from Smithy shape ``com.amazonaws.cloudformation#GeneratedTemplateDeletionPolicy``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

GeneratedTemplateDeletionPolicy: TypeAlias = Literal[
    "DELETE",
    "RETAIN",
]


# --- awsQuery ser/de ---
def to_query_text(value: GeneratedTemplateDeletionPolicy) -> str:
    return value


def from_query_text(text: str) -> GeneratedTemplateDeletionPolicy:
    return cast(GeneratedTemplateDeletionPolicy, text)


def serialize_query(
    value: GeneratedTemplateDeletionPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> GeneratedTemplateDeletionPolicy:
    return from_query_text(el.text or "")
