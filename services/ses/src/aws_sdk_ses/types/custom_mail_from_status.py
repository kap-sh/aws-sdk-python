"""Generated from Smithy shape ``com.amazonaws.ses#CustomMailFromStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

CustomMailFromStatus: TypeAlias = Literal[
    "Pending",
    "Success",
    "Failed",
    "TemporaryFailure",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Success",
        "Failed",
        "TemporaryFailure",
    )
)


def to_query_text(value: CustomMailFromStatus) -> str:
    return value


def from_query_text(text: str) -> CustomMailFromStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown CustomMailFromStatus value: {text!r}")
    return cast(CustomMailFromStatus, text)


def serialize_query(
    value: CustomMailFromStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> CustomMailFromStatus:
    return from_query_text(el.text or "")
