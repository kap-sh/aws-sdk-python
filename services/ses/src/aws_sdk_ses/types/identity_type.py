"""Generated from Smithy shape ``com.amazonaws.ses#IdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element

IdentityType: TypeAlias = Literal[
    "EmailAddress",
    "Domain",
]


# --- awsQuery ser/de ---
def to_query_text(value: IdentityType) -> str:
    return value


def from_query_text(text: str) -> IdentityType:
    return cast(IdentityType, text)


def serialize_query(
    value: IdentityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> IdentityType:
    return from_query_text(el.text or "")
