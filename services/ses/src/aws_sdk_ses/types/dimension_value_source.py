"""Generated from Smithy shape ``com.amazonaws.ses#DimensionValueSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element

DimensionValueSource: TypeAlias = Literal[
    "messageTag",
    "emailHeader",
    "linkTag",
]


# --- awsQuery ser/de ---
def to_query_text(value: DimensionValueSource) -> str:
    return value


def from_query_text(text: str) -> DimensionValueSource:
    return cast(DimensionValueSource, text)


def serialize_query(
    value: DimensionValueSource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DimensionValueSource:
    return from_query_text(el.text or "")
