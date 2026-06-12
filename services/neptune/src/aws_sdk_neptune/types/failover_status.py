"""Generated from Smithy shape ``com.amazonaws.neptune#FailoverStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune._protocol.xml import Element
from aws_sdk_neptune.errors import DeserializationError

FailoverStatus: TypeAlias = Literal[
    "pending",
    "failing-over",
    "cancelling",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pending",
        "failing-over",
        "cancelling",
    )
)


def to_query_text(value: FailoverStatus) -> str:
    return value


def from_query_text(text: str) -> FailoverStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown FailoverStatus value: {text!r}")
    return cast(FailoverStatus, text)


def serialize_query(
    value: FailoverStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> FailoverStatus:
    return from_query_text(el.text or "")
