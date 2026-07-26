"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationAction``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

StackSetOperationAction: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
    "DETECT_DRIFT",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackSetOperationAction) -> str:
    return value


def from_query_text(text: str) -> StackSetOperationAction:
    return cast(StackSetOperationAction, text)


def serialize_query(
    value: StackSetOperationAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackSetOperationAction:
    return from_query_text(el.text or "")
