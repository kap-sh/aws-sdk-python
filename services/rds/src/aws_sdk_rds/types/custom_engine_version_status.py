"""Generated from Smithy shape ``com.amazonaws.rds#CustomEngineVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

CustomEngineVersionStatus: TypeAlias = Literal[
    "available",
    "inactive",
    "inactive-except-restore",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "inactive",
        "inactive-except-restore",
    )
)


def to_query_text(value: CustomEngineVersionStatus) -> str:
    return value


def from_query_text(text: str) -> CustomEngineVersionStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CustomEngineVersionStatus value: {text!r}")
    return cast(CustomEngineVersionStatus, text)


def serialize_query(
    value: CustomEngineVersionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CustomEngineVersionStatus:
    return from_query_text(el.text or "")
