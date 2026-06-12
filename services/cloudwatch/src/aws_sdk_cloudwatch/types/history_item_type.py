"""Generated from Smithy shape ``com.amazonaws.cloudwatch#HistoryItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

HistoryItemType: TypeAlias = Literal[
    "ConfigurationUpdate",
    "StateUpdate",
    "Action",
    "AlarmContributorStateUpdate",
    "AlarmContributorAction",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConfigurationUpdate",
        "StateUpdate",
        "Action",
        "AlarmContributorStateUpdate",
        "AlarmContributorAction",
    )
)


def serialize_aws_json_1_0(value: HistoryItemType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HistoryItemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HistoryItemType value: {data!r}")
    return cast(HistoryItemType, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ConfigurationUpdate",
        "StateUpdate",
        "Action",
        "AlarmContributorStateUpdate",
        "AlarmContributorAction",
    )
)


def to_query_text(value: HistoryItemType) -> str:
    return value


def from_query_text(text: str) -> HistoryItemType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown HistoryItemType value: {text!r}")
    return cast(HistoryItemType, text)


def serialize_query(
    value: HistoryItemType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> HistoryItemType:
    return from_query_text(el.text or "")
