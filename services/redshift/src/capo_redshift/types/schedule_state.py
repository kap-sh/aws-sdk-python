"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduleState``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

ScheduleState: TypeAlias = Literal[
    "MODIFYING",
    "ACTIVE",
    "FAILED",
]


# --- awsQuery ser/de ---
def to_query_text(value: ScheduleState) -> str:
    return value


def from_query_text(text: str) -> ScheduleState:
    return cast(ScheduleState, text)


def serialize_query(
    value: ScheduleState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScheduleState:
    return from_query_text(el.text or "")
