"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

StatusCode: TypeAlias = Literal[
    "Complete",
    "InternalError",
    "PartialData",
    "Forbidden",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Complete",
        "InternalError",
        "PartialData",
        "Forbidden",
    )
)


def serialize_aws_json_1_0(value: StatusCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusCode value: {data!r}")
    return cast(StatusCode, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Complete",
        "InternalError",
        "PartialData",
        "Forbidden",
    )
)


def to_query_text(value: StatusCode) -> str:
    return value


def from_query_text(text: str) -> StatusCode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StatusCode value: {text!r}")
    return cast(StatusCode, text)


def serialize_query(
    value: StatusCode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StatusCode:
    return from_query_text(el.text or "")
