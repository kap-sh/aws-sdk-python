"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ActionsSuppressedBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

ActionsSuppressedBy: TypeAlias = Literal[
    "WaitPeriod",
    "ExtensionPeriod",
    "Alarm",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WaitPeriod",
        "ExtensionPeriod",
        "Alarm",
    )
)


def serialize_aws_json_1_0(value: ActionsSuppressedBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActionsSuppressedBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionsSuppressedBy value: {data!r}")
    return cast(ActionsSuppressedBy, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WaitPeriod",
        "ExtensionPeriod",
        "Alarm",
    )
)


def to_query_text(value: ActionsSuppressedBy) -> str:
    return value


def from_query_text(text: str) -> ActionsSuppressedBy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ActionsSuppressedBy value: {text!r}")
    return cast(ActionsSuppressedBy, text)


def serialize_query(
    value: ActionsSuppressedBy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ActionsSuppressedBy:
    return from_query_text(el.text or "")
