"""Generated from Smithy shape ``com.amazonaws.redshift#AquaConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

AquaConfigurationStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "auto",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
        "auto",
    )
)


def to_query_text(value: AquaConfigurationStatus) -> str:
    return value


def from_query_text(text: str) -> AquaConfigurationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AquaConfigurationStatus value: {text!r}")
    return cast(AquaConfigurationStatus, text)


def serialize_query(
    value: AquaConfigurationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AquaConfigurationStatus:
    return from_query_text(el.text or "")
