"""Generated from Smithy shape ``com.amazonaws.elasticache#LogDeliveryConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

LogDeliveryConfigurationStatus: TypeAlias = Literal[
    "active",
    "enabling",
    "modifying",
    "disabling",
    "error",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "enabling",
        "modifying",
        "disabling",
        "error",
    )
)


def to_query_text(value: LogDeliveryConfigurationStatus) -> str:
    return value


def from_query_text(text: str) -> LogDeliveryConfigurationStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown LogDeliveryConfigurationStatus value: {text!r}"
        )
    return cast(LogDeliveryConfigurationStatus, text)


def serialize_query(
    value: LogDeliveryConfigurationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LogDeliveryConfigurationStatus:
    return from_query_text(el.text or "")
