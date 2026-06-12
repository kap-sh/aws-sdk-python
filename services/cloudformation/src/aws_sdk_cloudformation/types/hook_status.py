"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

HookStatus: TypeAlias = Literal[
    "HOOK_IN_PROGRESS",
    "HOOK_COMPLETE_SUCCEEDED",
    "HOOK_COMPLETE_FAILED",
    "HOOK_FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOOK_IN_PROGRESS",
        "HOOK_COMPLETE_SUCCEEDED",
        "HOOK_COMPLETE_FAILED",
        "HOOK_FAILED",
    )
)


def to_query_text(value: HookStatus) -> str:
    return value


def from_query_text(text: str) -> HookStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HookStatus value: {text!r}")
    return cast(HookStatus, text)


def serialize_query(
    value: HookStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HookStatus:
    return from_query_text(el.text or "")
