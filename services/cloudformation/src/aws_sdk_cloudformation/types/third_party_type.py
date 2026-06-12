"""Generated from Smithy shape ``com.amazonaws.cloudformation#ThirdPartyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ThirdPartyType: TypeAlias = Literal[
    "RESOURCE",
    "MODULE",
    "HOOK",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE",
        "MODULE",
        "HOOK",
    )
)


def to_query_text(value: ThirdPartyType) -> str:
    return value


def from_query_text(text: str) -> ThirdPartyType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ThirdPartyType value: {text!r}")
    return cast(ThirdPartyType, text)


def serialize_query(
    value: ThirdPartyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ThirdPartyType:
    return from_query_text(el.text or "")
