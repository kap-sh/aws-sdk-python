"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetDriftStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

StackSetDriftStatus: TypeAlias = Literal[
    "DRIFTED",
    "IN_SYNC",
    "NOT_CHECKED",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackSetDriftStatus) -> str:
    return value


def from_query_text(text: str) -> StackSetDriftStatus:
    return cast(StackSetDriftStatus, text)


def serialize_query(
    value: StackSetDriftStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackSetDriftStatus:
    return from_query_text(el.text or "")
