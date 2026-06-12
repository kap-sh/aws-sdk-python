"""Generated from Smithy shape ``com.amazonaws.cloudwatch#RecentlyActive``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

RecentlyActive: TypeAlias = Literal["PT3H",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("PT3H",))


def serialize_aws_json_1_0(value: RecentlyActive) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RecentlyActive:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecentlyActive value: {data!r}")
    return cast(RecentlyActive, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("PT3H",))


def to_query_text(value: RecentlyActive) -> str:
    return value


def from_query_text(text: str) -> RecentlyActive:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RecentlyActive value: {text!r}")
    return cast(RecentlyActive, text)


def serialize_query(
    value: RecentlyActive, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RecentlyActive:
    return from_query_text(el.text or "")
