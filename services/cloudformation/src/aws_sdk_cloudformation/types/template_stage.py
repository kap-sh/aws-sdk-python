"""Generated from Smithy shape ``com.amazonaws.cloudformation#TemplateStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

TemplateStage: TypeAlias = Literal[
    "Original",
    "Processed",
]


# --- awsQuery ser/de ---
def to_query_text(value: TemplateStage) -> str:
    return value


def from_query_text(text: str) -> TemplateStage:
    return cast(TemplateStage, text)


def serialize_query(
    value: TemplateStage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TemplateStage:
    return from_query_text(el.text or "")
