"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceFilterName``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

StackInstanceFilterName: TypeAlias = Literal[
    "DETAILED_STATUS",
    "LAST_OPERATION_ID",
    "DRIFT_STATUS",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackInstanceFilterName) -> str:
    return value


def from_query_text(text: str) -> StackInstanceFilterName:
    return cast(StackInstanceFilterName, text)


def serialize_query(
    value: StackInstanceFilterName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackInstanceFilterName:
    return from_query_text(el.text or "")
