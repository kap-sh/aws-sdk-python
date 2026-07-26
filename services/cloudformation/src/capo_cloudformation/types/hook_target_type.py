"""Generated from Smithy shape ``com.amazonaws.cloudformation#HookTargetType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

HookTargetType: TypeAlias = Literal["RESOURCE",]


# --- awsQuery ser/de ---
def to_query_text(value: HookTargetType) -> str:
    return value


def from_query_text(text: str) -> HookTargetType:
    return cast(HookTargetType, text)


def serialize_query(
    value: HookTargetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HookTargetType:
    return from_query_text(el.text or "")
