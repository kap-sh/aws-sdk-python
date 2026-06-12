"""Generated from Smithy shape ``com.amazonaws.redshift#ServiceAuthorization``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ServiceAuthorization: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def to_query_text(value: ServiceAuthorization) -> str:
    return value


def from_query_text(text: str) -> ServiceAuthorization:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ServiceAuthorization value: {text!r}")
    return cast(ServiceAuthorization, text)


def serialize_query(
    value: ServiceAuthorization, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ServiceAuthorization:
    return from_query_text(el.text or "")
