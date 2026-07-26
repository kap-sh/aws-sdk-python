"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookTargetAction``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

HookTargetAction: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
    "IMPORT",
]


# --- awsQuery ser/de ---
def to_query_text(value: HookTargetAction) -> str:
    return value


def from_query_text(text: str) -> HookTargetAction:
    return cast(HookTargetAction, text)


def serialize_query(
    value: HookTargetAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HookTargetAction:
    return from_query_text(el.text or "")
