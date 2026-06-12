"""Generated from Smithy shape ``com.amazonaws.cloudformation#BeforeValueFrom``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

BeforeValueFrom: TypeAlias = Literal[
    "PREVIOUS_DEPLOYMENT_STATE",
    "ACTUAL_STATE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREVIOUS_DEPLOYMENT_STATE",
        "ACTUAL_STATE",
    )
)


def to_query_text(value: BeforeValueFrom) -> str:
    return value


def from_query_text(text: str) -> BeforeValueFrom:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BeforeValueFrom value: {text!r}")
    return cast(BeforeValueFrom, text)


def serialize_query(
    value: BeforeValueFrom, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BeforeValueFrom:
    return from_query_text(el.text or "")
