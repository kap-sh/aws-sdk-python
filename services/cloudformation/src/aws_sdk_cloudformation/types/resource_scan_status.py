"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceScanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ResourceScanStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "COMPLETE",
    "EXPIRED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "COMPLETE",
        "EXPIRED",
    )
)


def to_query_text(value: ResourceScanStatus) -> str:
    return value


def from_query_text(text: str) -> ResourceScanStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ResourceScanStatus value: {text!r}")
    return cast(ResourceScanStatus, text)


def serialize_query(
    value: ResourceScanStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ResourceScanStatus:
    return from_query_text(el.text or "")
