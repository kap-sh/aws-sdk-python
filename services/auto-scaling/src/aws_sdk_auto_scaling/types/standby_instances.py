"""Generated from Smithy shape ``com.amazonaws.autoscaling#StandbyInstances``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

StandbyInstances: TypeAlias = Literal[
    "Terminate",
    "Ignore",
    "Wait",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Terminate",
        "Ignore",
        "Wait",
    )
)


def to_query_text(value: StandbyInstances) -> str:
    return value


def from_query_text(text: str) -> StandbyInstances:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StandbyInstances value: {text!r}")
    return cast(StandbyInstances, text)


def serialize_query(
    value: StandbyInstances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StandbyInstances:
    return from_query_text(el.text or "")
