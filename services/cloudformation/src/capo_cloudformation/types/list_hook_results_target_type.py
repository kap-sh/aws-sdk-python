"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListHookResultsTargetType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

ListHookResultsTargetType: TypeAlias = Literal[
    "CHANGE_SET",
    "STACK",
    "RESOURCE",
    "CLOUD_CONTROL",
]


# --- awsQuery ser/de ---
def to_query_text(value: ListHookResultsTargetType) -> str:
    return value


def from_query_text(text: str) -> ListHookResultsTargetType:
    return cast(ListHookResultsTargetType, text)


def serialize_query(
    value: ListHookResultsTargetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ListHookResultsTargetType:
    return from_query_text(el.text or "")
