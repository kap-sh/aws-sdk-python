"""Generated from Smithy shape ``com.amazonaws.ses#DsnAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

DsnAction: TypeAlias = Literal[
    "failed",
    "delayed",
    "delivered",
    "relayed",
    "expanded",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "failed",
        "delayed",
        "delivered",
        "relayed",
        "expanded",
    )
)


def to_query_text(value: DsnAction) -> str:
    return value


def from_query_text(text: str) -> DsnAction:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DsnAction value: {text!r}")
    return cast(DsnAction, text)


def serialize_query(
    value: DsnAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DsnAction:
    return from_query_text(el.text or "")
