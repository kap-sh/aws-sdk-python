"""Generated from Smithy shape ``com.amazonaws.autoscaling#StandbyInstances``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

StandbyInstances: TypeAlias = Literal[
    "Terminate",
    "Ignore",
    "Wait",
]


# --- awsQuery ser/de ---
def to_query_text(value: StandbyInstances) -> str:
    return value


def from_query_text(text: str) -> StandbyInstances:
    return cast(StandbyInstances, text)


def serialize_query(
    value: StandbyInstances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StandbyInstances:
    return from_query_text(el.text or "")
