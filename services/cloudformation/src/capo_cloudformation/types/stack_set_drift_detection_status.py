"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetDriftDetectionStatus``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

StackSetDriftDetectionStatus: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
    "PARTIAL_SUCCESS",
    "IN_PROGRESS",
    "STOPPED",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackSetDriftDetectionStatus) -> str:
    return value


def from_query_text(text: str) -> StackSetDriftDetectionStatus:
    return cast(StackSetDriftDetectionStatus, text)


def serialize_query(
    value: StackSetDriftDetectionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackSetDriftDetectionStatus:
    return from_query_text(el.text or "")
