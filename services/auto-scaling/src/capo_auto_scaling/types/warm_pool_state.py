"""Generated from Smithy shape ``com.amazonaws.autoscaling#WarmPoolState``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

WarmPoolState: TypeAlias = Literal[
    "Stopped",
    "Running",
    "Hibernated",
]


# --- awsQuery ser/de ---
def to_query_text(value: WarmPoolState) -> str:
    return value


def from_query_text(text: str) -> WarmPoolState:
    return cast(WarmPoolState, text)


def serialize_query(
    value: WarmPoolState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> WarmPoolState:
    return from_query_text(el.text or "")
