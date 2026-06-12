"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceGeneration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

InstanceGeneration: TypeAlias = Literal[
    "current",
    "previous",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "current",
        "previous",
    )
)


def to_query_text(value: InstanceGeneration) -> str:
    return value


def from_query_text(text: str) -> InstanceGeneration:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InstanceGeneration value: {text!r}")
    return cast(InstanceGeneration, text)


def serialize_query(
    value: InstanceGeneration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InstanceGeneration:
    return from_query_text(el.text or "")
