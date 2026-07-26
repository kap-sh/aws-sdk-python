"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateActionStatus``."""

from typing import Literal, TypeAlias, cast

from capo_elasticache._protocol.xml import Element

UpdateActionStatus: TypeAlias = Literal[
    "not-applied",
    "waiting-to-start",
    "in-progress",
    "stopping",
    "stopped",
    "complete",
    "scheduling",
    "scheduled",
    "not-applicable",
]


# --- awsQuery ser/de ---
def to_query_text(value: UpdateActionStatus) -> str:
    return value


def from_query_text(text: str) -> UpdateActionStatus:
    return cast(UpdateActionStatus, text)


def serialize_query(
    value: UpdateActionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> UpdateActionStatus:
    return from_query_text(el.text or "")
