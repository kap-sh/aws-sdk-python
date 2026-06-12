"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookInvocationPoint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

HookInvocationPoint: TypeAlias = Literal["PRE_PROVISION",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("PRE_PROVISION",))


def to_query_text(value: HookInvocationPoint) -> str:
    return value


def from_query_text(text: str) -> HookInvocationPoint:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HookInvocationPoint value: {text!r}")
    return cast(HookInvocationPoint, text)


def serialize_query(
    value: HookInvocationPoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HookInvocationPoint:
    return from_query_text(el.text or "")
