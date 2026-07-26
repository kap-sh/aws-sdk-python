"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionTypeValues``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

ScheduledActionTypeValues: TypeAlias = Literal[
    "ResizeCluster",
    "PauseCluster",
    "ResumeCluster",
]


# --- awsQuery ser/de ---
def to_query_text(value: ScheduledActionTypeValues) -> str:
    return value


def from_query_text(text: str) -> ScheduledActionTypeValues:
    return cast(ScheduledActionTypeValues, text)


def serialize_query(
    value: ScheduledActionTypeValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScheduledActionTypeValues:
    return from_query_text(el.text or "")
