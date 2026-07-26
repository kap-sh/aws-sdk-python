"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorDetection``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

StackRefactorDetection: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackRefactorDetection) -> str:
    return value


def from_query_text(text: str) -> StackRefactorDetection:
    return cast(StackRefactorDetection, text)


def serialize_query(
    value: StackRefactorDetection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackRefactorDetection:
    return from_query_text(el.text or "")
