"""Generated from Smithy shape ``com.amazonaws.iam#encodingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

encodingType: TypeAlias = Literal[
    "SSH",
    "PEM",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSH",
        "PEM",
    )
)


def to_query_text(value: encodingType) -> str:
    return value


def from_query_text(text: str) -> encodingType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown encodingType value: {text!r}")
    return cast(encodingType, text)


def serialize_query(
    value: encodingType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> encodingType:
    return from_query_text(el.text or "")
