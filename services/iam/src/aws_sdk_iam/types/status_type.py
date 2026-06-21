"""Generated from Smithy shape ``com.amazonaws.iam#statusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

statusType: TypeAlias = Literal[
    "Active",
    "Inactive",
    "Expired",
]


# --- awsQuery ser/de ---
def to_query_text(value: statusType) -> str:
    return value


def from_query_text(text: str) -> statusType:
    return cast(statusType, text)


def serialize_query(
    value: statusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> statusType:
    return from_query_text(el.text or "")
