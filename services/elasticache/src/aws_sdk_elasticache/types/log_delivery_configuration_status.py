"""Generated from Smithy shape ``com.amazonaws.elasticache#LogDeliveryConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

LogDeliveryConfigurationStatus: TypeAlias = Literal[
    "active",
    "enabling",
    "modifying",
    "disabling",
    "error",
]


# --- awsQuery ser/de ---
def to_query_text(value: LogDeliveryConfigurationStatus) -> str:
    return value


def from_query_text(text: str) -> LogDeliveryConfigurationStatus:
    return cast(LogDeliveryConfigurationStatus, text)


def serialize_query(
    value: LogDeliveryConfigurationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LogDeliveryConfigurationStatus:
    return from_query_text(el.text or "")
