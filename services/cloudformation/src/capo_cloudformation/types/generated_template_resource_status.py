"""Generated from Smithy shape ``com.amazonaws.cloudformation#GeneratedTemplateResourceStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

GeneratedTemplateResourceStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETE",
]


# --- awsQuery ser/de ---
def to_query_text(value: GeneratedTemplateResourceStatus) -> str:
    return value


def from_query_text(text: str) -> GeneratedTemplateResourceStatus:
    return cast(GeneratedTemplateResourceStatus, text)


def serialize_query(
    value: GeneratedTemplateResourceStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> GeneratedTemplateResourceStatus:
    return from_query_text(el.text or "")
