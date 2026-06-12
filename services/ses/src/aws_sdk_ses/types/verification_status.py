"""Generated from Smithy shape ``com.amazonaws.ses#VerificationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

VerificationStatus: TypeAlias = Literal[
    "Pending",
    "Success",
    "Failed",
    "TemporaryFailure",
    "NotStarted",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Success",
        "Failed",
        "TemporaryFailure",
        "NotStarted",
    )
)


def to_query_text(value: VerificationStatus) -> str:
    return value


def from_query_text(text: str) -> VerificationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown VerificationStatus value: {text!r}")
    return cast(VerificationStatus, text)


def serialize_query(
    value: VerificationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> VerificationStatus:
    return from_query_text(el.text or "")
