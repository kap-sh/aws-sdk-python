"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

DataShareStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_AUTHORIZATION",
    "AUTHORIZED",
    "DEAUTHORIZED",
    "REJECTED",
    "AVAILABLE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PENDING_AUTHORIZATION",
        "AUTHORIZED",
        "DEAUTHORIZED",
        "REJECTED",
        "AVAILABLE",
    )
)


def to_query_text(value: DataShareStatus) -> str:
    return value


def from_query_text(text: str) -> DataShareStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DataShareStatus value: {text!r}")
    return cast(DataShareStatus, text)


def serialize_query(
    value: DataShareStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataShareStatus:
    return from_query_text(el.text or "")
