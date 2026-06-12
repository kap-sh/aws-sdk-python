"""Generated from Smithy shape ``com.amazonaws.redshift#AquaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

AquaStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
    "applying",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
        "applying",
    )
)


def to_query_text(value: AquaStatus) -> str:
    return value


def from_query_text(text: str) -> AquaStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AquaStatus value: {text!r}")
    return cast(AquaStatus, text)


def serialize_query(
    value: AquaStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AquaStatus:
    return from_query_text(el.text or "")
