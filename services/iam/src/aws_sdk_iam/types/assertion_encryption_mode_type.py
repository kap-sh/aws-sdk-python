"""Generated from Smithy shape ``com.amazonaws.iam#assertionEncryptionModeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

assertionEncryptionModeType: TypeAlias = Literal[
    "Required",
    "Allowed",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Required",
        "Allowed",
    )
)


def to_query_text(value: assertionEncryptionModeType) -> str:
    return value


def from_query_text(text: str) -> assertionEncryptionModeType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown assertionEncryptionModeType value: {text!r}"
        )
    return cast(assertionEncryptionModeType, text)


def serialize_query(
    value: assertionEncryptionModeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> assertionEncryptionModeType:
    return from_query_text(el.text or "")
