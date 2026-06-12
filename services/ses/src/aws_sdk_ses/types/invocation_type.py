"""Generated from Smithy shape ``com.amazonaws.ses#InvocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

InvocationType: TypeAlias = Literal[
    "Event",
    "RequestResponse",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Event",
        "RequestResponse",
    )
)


def to_query_text(value: InvocationType) -> str:
    return value


def from_query_text(text: str) -> InvocationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InvocationType value: {text!r}")
    return cast(InvocationType, text)


def serialize_query(
    value: InvocationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InvocationType:
    return from_query_text(el.text or "")
