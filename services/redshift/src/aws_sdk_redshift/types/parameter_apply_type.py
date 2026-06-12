"""Generated from Smithy shape ``com.amazonaws.redshift#ParameterApplyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

ParameterApplyType: TypeAlias = Literal[
    "static",
    "dynamic",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "static",
        "dynamic",
    )
)


def to_query_text(value: ParameterApplyType) -> str:
    return value


def from_query_text(text: str) -> ParameterApplyType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ParameterApplyType value: {text!r}")
    return cast(ParameterApplyType, text)


def serialize_query(
    value: ParameterApplyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ParameterApplyType:
    return from_query_text(el.text or "")
