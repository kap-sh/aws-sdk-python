"""Generated from Smithy shape ``com.amazonaws.elasticache#InputAuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

InputAuthenticationType: TypeAlias = Literal[
    "password",
    "no-password-required",
    "iam",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "password",
        "no-password-required",
        "iam",
    )
)


def to_query_text(value: InputAuthenticationType) -> str:
    return value


def from_query_text(text: str) -> InputAuthenticationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown InputAuthenticationType value: {text!r}")
    return cast(InputAuthenticationType, text)


def serialize_query(
    value: InputAuthenticationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> InputAuthenticationType:
    return from_query_text(el.text or "")
