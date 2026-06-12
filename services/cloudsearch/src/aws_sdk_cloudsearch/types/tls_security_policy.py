"""Generated from Smithy shape ``com.amazonaws.cloudsearch#TLSSecurityPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

"""<p>The minimum required TLS version.</p>"""
TLSSecurityPolicy: TypeAlias = Literal[
    "Policy-Min-TLS-1-0-2019-07",
    "Policy-Min-TLS-1-2-2019-07",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Policy-Min-TLS-1-0-2019-07",
        "Policy-Min-TLS-1-2-2019-07",
    )
)


def to_query_text(value: TLSSecurityPolicy) -> str:
    return value


def from_query_text(text: str) -> TLSSecurityPolicy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TLSSecurityPolicy value: {text!r}")
    return cast(TLSSecurityPolicy, text)


def serialize_query(
    value: TLSSecurityPolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TLSSecurityPolicy:
    return from_query_text(el.text or "")
