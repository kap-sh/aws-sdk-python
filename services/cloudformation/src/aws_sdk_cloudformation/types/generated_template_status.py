"""Generated from Smithy shape ``com.amazonaws.cloudformation#GeneratedTemplateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

GeneratedTemplateStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "UPDATE_PENDING",
    "DELETE_PENDING",
    "CREATE_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "FAILED",
    "COMPLETE",
]


# --- awsQuery ser/de ---
def to_query_text(value: GeneratedTemplateStatus) -> str:
    return value


def from_query_text(text: str) -> GeneratedTemplateStatus:
    return cast(GeneratedTemplateStatus, text)


def serialize_query(
    value: GeneratedTemplateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> GeneratedTemplateStatus:
    return from_query_text(el.text or "")
