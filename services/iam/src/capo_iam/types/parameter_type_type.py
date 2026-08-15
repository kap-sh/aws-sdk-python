"""Generated from Smithy shape ``com.amazonaws.iam#parameterTypeType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

parameterTypeType: TypeAlias = Literal[
    "String",
    "StringList",
    "Number",
    "NumberList",
    "Arn",
    "ArnList",
]


# --- awsQuery ser/de ---
def to_query_text(value: parameterTypeType) -> str:
    return value


def from_query_text(text: str) -> parameterTypeType:
    return cast(parameterTypeType, text)


def serialize_query(
    value: parameterTypeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> parameterTypeType:
    return from_query_text(el.text or "")
