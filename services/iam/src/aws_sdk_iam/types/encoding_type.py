"""Generated from Smithy shape ``com.amazonaws.iam#encodingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

encodingType: TypeAlias = Literal[
    "SSH",
    "PEM",
]


# --- awsQuery ser/de ---
def to_query_text(value: encodingType) -> str:
    return value


def from_query_text(text: str) -> encodingType:
    return cast(encodingType, text)


def serialize_query(
    value: encodingType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> encodingType:
    return from_query_text(el.text or "")
