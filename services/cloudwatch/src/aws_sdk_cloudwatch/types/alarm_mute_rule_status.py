"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmMuteRuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

AlarmMuteRuleStatus: TypeAlias = Literal[
    "SCHEDULED",
    "ACTIVE",
    "EXPIRED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "ACTIVE",
        "EXPIRED",
    )
)


def serialize_aws_json_1_0(value: AlarmMuteRuleStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AlarmMuteRuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlarmMuteRuleStatus value: {data!r}")
    return cast(AlarmMuteRuleStatus, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "ACTIVE",
        "EXPIRED",
    )
)


def to_query_text(value: AlarmMuteRuleStatus) -> str:
    return value


def from_query_text(text: str) -> AlarmMuteRuleStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AlarmMuteRuleStatus value: {text!r}")
    return cast(AlarmMuteRuleStatus, text)


def serialize_query(
    value: AlarmMuteRuleStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AlarmMuteRuleStatus:
    return from_query_text(el.text or "")
