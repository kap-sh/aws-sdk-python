"""Generated from Smithy shape ``com.amazonaws.cloudformation#AfterValueFrom``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

AfterValueFrom: TypeAlias = Literal["TEMPLATE",]


# --- awsQuery ser/de ---
def to_query_text(value: AfterValueFrom) -> str:
    return value


def from_query_text(text: str) -> AfterValueFrom:
    return cast(AfterValueFrom, text)


def serialize_query(
    value: AfterValueFrom, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AfterValueFrom:
    return from_query_text(el.text or "")
