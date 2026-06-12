"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ValidationSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

ValidationSeverity: TypeAlias = Literal[
    "error",
    "warning",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "error",
        "warning",
    )
)


def to_query_text(value: ValidationSeverity) -> str:
    return value


def from_query_text(text: str) -> ValidationSeverity:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ValidationSeverity value: {text!r}")
    return cast(ValidationSeverity, text)


def serialize_query(
    value: ValidationSeverity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ValidationSeverity:
    return from_query_text(el.text or "")
