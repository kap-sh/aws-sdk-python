"""Generated from Smithy shape ``com.amazonaws.elasticache#TransitEncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element

TransitEncryptionMode: TypeAlias = Literal[
    "preferred",
    "required",
]


# --- awsQuery ser/de ---
def to_query_text(value: TransitEncryptionMode) -> str:
    return value


def from_query_text(text: str) -> TransitEncryptionMode:
    return cast(TransitEncryptionMode, text)


def serialize_query(
    value: TransitEncryptionMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TransitEncryptionMode:
    return from_query_text(el.text or "")
