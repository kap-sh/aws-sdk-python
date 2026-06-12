"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

HookTargetType: TypeAlias = Literal["RESOURCE",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("RESOURCE",))


def to_query_text(value: HookTargetType) -> str:
    return value


def from_query_text(text: str) -> HookTargetType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HookTargetType value: {text!r}")
    return cast(HookTargetType, text)


def serialize_query(
    value: HookTargetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HookTargetType:
    return from_query_text(el.text or "")
