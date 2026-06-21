"""Generated from Smithy shape ``com.amazonaws.cloudformation#WarningType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

WarningType: TypeAlias = Literal[
    "MUTUALLY_EXCLUSIVE_PROPERTIES",
    "UNSUPPORTED_PROPERTIES",
    "MUTUALLY_EXCLUSIVE_TYPES",
    "EXCLUDED_PROPERTIES",
    "EXCLUDED_RESOURCES",
]


# --- awsQuery ser/de ---
def to_query_text(value: WarningType) -> str:
    return value


def from_query_text(text: str) -> WarningType:
    return cast(WarningType, text)


def serialize_query(
    value: WarningType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> WarningType:
    return from_query_text(el.text or "")
