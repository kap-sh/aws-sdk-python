"""Generated from Smithy shape ``com.amazonaws.ec2#StatisticType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

StatisticType: TypeAlias = Literal["p50",]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(("p50",))


_VALUES: frozenset[str] = frozenset(("p50",))


def to_ec2_query_text(value: StatisticType) -> str:
    return value


def from_ec2_query_text(text: str) -> StatisticType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StatisticType value: {text!r}")
    return cast(StatisticType, text)


def serialize_ec2_query(
    value: StatisticType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> StatisticType:
    return from_ec2_query_text(el.text or "")
