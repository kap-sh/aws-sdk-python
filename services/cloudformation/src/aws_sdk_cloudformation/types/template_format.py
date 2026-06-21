"""Generated from Smithy shape ``com.amazonaws.cloudformation#TemplateFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

TemplateFormat: TypeAlias = Literal[
    "JSON",
    "YAML",
]


# --- awsQuery ser/de ---
def to_query_text(value: TemplateFormat) -> str:
    return value


def from_query_text(text: str) -> TemplateFormat:
    return cast(TemplateFormat, text)


def serialize_query(
    value: TemplateFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TemplateFormat:
    return from_query_text(el.text or "")
