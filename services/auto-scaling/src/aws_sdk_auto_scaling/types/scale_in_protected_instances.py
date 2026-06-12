"""Generated from Smithy shape ``com.amazonaws.autoscaling#ScaleInProtectedInstances``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

ScaleInProtectedInstances: TypeAlias = Literal[
    "Refresh",
    "Ignore",
    "Wait",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Refresh",
        "Ignore",
        "Wait",
    )
)


def to_query_text(value: ScaleInProtectedInstances) -> str:
    return value


def from_query_text(text: str) -> ScaleInProtectedInstances:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ScaleInProtectedInstances value: {text!r}")
    return cast(ScaleInProtectedInstances, text)


def serialize_query(
    value: ScaleInProtectedInstances, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScaleInProtectedInstances:
    return from_query_text(el.text or "")
