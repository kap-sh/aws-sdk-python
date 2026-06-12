"""Generated from Smithy shape ``com.amazonaws.autoscaling#RetentionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

RetentionAction: TypeAlias = Literal[
    "retain",
    "terminate",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "retain",
        "terminate",
    )
)


def to_query_text(value: RetentionAction) -> str:
    return value


def from_query_text(text: str) -> RetentionAction:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RetentionAction value: {text!r}")
    return cast(RetentionAction, text)


def serialize_query(
    value: RetentionAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RetentionAction:
    return from_query_text(el.text or "")
