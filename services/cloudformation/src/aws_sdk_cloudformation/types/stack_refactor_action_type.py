"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

StackRefactorActionType: TypeAlias = Literal[
    "MOVE",
    "CREATE",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackRefactorActionType) -> str:
    return value


def from_query_text(text: str) -> StackRefactorActionType:
    return cast(StackRefactorActionType, text)


def serialize_query(
    value: StackRefactorActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackRefactorActionType:
    return from_query_text(el.text or "")
