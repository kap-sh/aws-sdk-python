"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionTypeValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ScheduledActionTypeValues: TypeAlias = Literal[
    "ResizeCluster",
    "PauseCluster",
    "ResumeCluster",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ResizeCluster",
        "PauseCluster",
        "ResumeCluster",
    )
)


def to_query_text(value: ScheduledActionTypeValues) -> str:
    return value


def from_query_text(text: str) -> ScheduledActionTypeValues:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ScheduledActionTypeValues value: {text!r}")
    return cast(ScheduledActionTypeValues, text)


def serialize_query(
    value: ScheduledActionTypeValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScheduledActionTypeValues:
    return from_query_text(el.text or "")
