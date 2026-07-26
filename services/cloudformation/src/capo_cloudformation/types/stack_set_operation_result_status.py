"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationResultStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

StackSetOperationResultStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLED",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackSetOperationResultStatus) -> str:
    return value


def from_query_text(text: str) -> StackSetOperationResultStatus:
    return cast(StackSetOperationResultStatus, text)


def serialize_query(
    value: StackSetOperationResultStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackSetOperationResultStatus:
    return from_query_text(el.text or "")
