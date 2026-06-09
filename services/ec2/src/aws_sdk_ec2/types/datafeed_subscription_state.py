"""Generated from Smithy shape ``com.amazonaws.ec2#DatafeedSubscriptionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ec2._protocol.xml import Element
from aws_sdk_ec2.errors import DeserializationError

DatafeedSubscriptionState: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def to_ec2_query_text(value: DatafeedSubscriptionState) -> str:
    return value


def from_ec2_query_text(text: str) -> DatafeedSubscriptionState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DatafeedSubscriptionState value: {text!r}")
    return cast(DatafeedSubscriptionState, text)


def serialize_ec2_query(
    value: DatafeedSubscriptionState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> DatafeedSubscriptionState:
    return from_ec2_query_text(el.text or "")
