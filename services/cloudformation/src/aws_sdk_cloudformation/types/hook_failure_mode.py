"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookFailureMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

HookFailureMode: TypeAlias = Literal[
    "FAIL",
    "WARN",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAIL",
        "WARN",
    )
)


def to_query_text(value: HookFailureMode) -> str:
    return value


def from_query_text(text: str) -> HookFailureMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HookFailureMode value: {text!r}")
    return cast(HookFailureMode, text)


def serialize_query(
    value: HookFailureMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HookFailureMode:
    return from_query_text(el.text or "")
