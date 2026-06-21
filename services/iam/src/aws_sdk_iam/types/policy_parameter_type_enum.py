"""Generated from Smithy shape ``com.amazonaws.iam#PolicyParameterTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

PolicyParameterTypeEnum: TypeAlias = Literal[
    "string",
    "stringList",
]


# --- awsQuery ser/de ---
def to_query_text(value: PolicyParameterTypeEnum) -> str:
    return value


def from_query_text(text: str) -> PolicyParameterTypeEnum:
    return cast(PolicyParameterTypeEnum, text)


def serialize_query(
    value: PolicyParameterTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PolicyParameterTypeEnum:
    return from_query_text(el.text or "")
