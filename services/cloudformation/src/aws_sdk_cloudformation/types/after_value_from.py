"""Generated from Smithy shape ``com.amazonaws.cloudformation#AfterValueFrom``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

AfterValueFrom: TypeAlias = Literal["TEMPLATE",]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(("TEMPLATE",))


def to_query_text(value: AfterValueFrom) -> str:
    return value


def from_query_text(text: str) -> AfterValueFrom:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AfterValueFrom value: {text!r}")
    return cast(AfterValueFrom, text)


def serialize_query(
    value: AfterValueFrom, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AfterValueFrom:
    return from_query_text(el.text or "")
