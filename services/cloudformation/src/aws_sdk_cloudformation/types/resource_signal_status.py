"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceSignalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ResourceSignalStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILURE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILURE",
    )
)


def to_query_text(value: ResourceSignalStatus) -> str:
    return value


def from_query_text(text: str) -> ResourceSignalStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ResourceSignalStatus value: {text!r}")
    return cast(ResourceSignalStatus, text)


def serialize_query(
    value: ResourceSignalStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ResourceSignalStatus:
    return from_query_text(el.text or "")
