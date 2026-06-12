"""Generated from Smithy shape ``com.amazonaws.cloudformation#GeneratedTemplateUpdateReplacePolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

GeneratedTemplateUpdateReplacePolicy: TypeAlias = Literal[
    "DELETE",
    "RETAIN",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE",
        "RETAIN",
    )
)


def to_query_text(value: GeneratedTemplateUpdateReplacePolicy) -> str:
    return value


def from_query_text(text: str) -> GeneratedTemplateUpdateReplacePolicy:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown GeneratedTemplateUpdateReplacePolicy value: {text!r}"
        )
    return cast(GeneratedTemplateUpdateReplacePolicy, text)


def serialize_query(
    value: GeneratedTemplateUpdateReplacePolicy,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> GeneratedTemplateUpdateReplacePolicy:
    return from_query_text(el.text or "")
