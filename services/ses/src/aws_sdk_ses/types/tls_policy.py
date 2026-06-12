"""Generated from Smithy shape ``com.amazonaws.ses#TlsPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

TlsPolicy: TypeAlias = Literal[
    "Require",
    "Optional",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Require",
        "Optional",
    )
)


def to_query_text(value: TlsPolicy) -> str:
    return value


def from_query_text(text: str) -> TlsPolicy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TlsPolicy value: {text!r}")
    return cast(TlsPolicy, text)


def serialize_query(
    value: TlsPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TlsPolicy:
    return from_query_text(el.text or "")
