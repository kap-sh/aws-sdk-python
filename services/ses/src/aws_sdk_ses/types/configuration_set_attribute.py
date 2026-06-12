"""Generated from Smithy shape ``com.amazonaws.ses#ConfigurationSetAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

ConfigurationSetAttribute: TypeAlias = Literal[
    "eventDestinations",
    "trackingOptions",
    "deliveryOptions",
    "reputationOptions",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "eventDestinations",
        "trackingOptions",
        "deliveryOptions",
        "reputationOptions",
    )
)


def to_query_text(value: ConfigurationSetAttribute) -> str:
    return value


def from_query_text(text: str) -> ConfigurationSetAttribute:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationSetAttribute value: {text!r}")
    return cast(ConfigurationSetAttribute, text)


def serialize_query(
    value: ConfigurationSetAttribute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ConfigurationSetAttribute:
    return from_query_text(el.text or "")
