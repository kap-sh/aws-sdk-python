"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookTargetAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

HookTargetAction: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
    "IMPORT",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE",
        "UPDATE",
        "DELETE",
        "IMPORT",
    )
)


def to_query_text(value: HookTargetAction) -> str:
    return value


def from_query_text(text: str) -> HookTargetAction:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HookTargetAction value: {text!r}")
    return cast(HookTargetAction, text)


def serialize_query(
    value: HookTargetAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HookTargetAction:
    return from_query_text(el.text or "")
