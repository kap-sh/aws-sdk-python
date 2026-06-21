"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackDriftDetectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

StackDriftDetectionStatus: TypeAlias = Literal[
    "DETECTION_IN_PROGRESS",
    "DETECTION_FAILED",
    "DETECTION_COMPLETE",
]


# --- awsQuery ser/de ---
def to_query_text(value: StackDriftDetectionStatus) -> str:
    return value


def from_query_text(text: str) -> StackDriftDetectionStatus:
    return cast(StackDriftDetectionStatus, text)


def serialize_query(
    value: StackDriftDetectionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackDriftDetectionStatus:
    return from_query_text(el.text or "")
