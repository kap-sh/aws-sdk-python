"""Generated from Smithy shape ``com.amazonaws.ses#BounceType``."""

from typing import Literal, TypeAlias, cast

from capo_ses._protocol.xml import Element

BounceType: TypeAlias = Literal[
    "DoesNotExist",
    "MessageTooLarge",
    "ExceededQuota",
    "ContentRejected",
    "Undefined",
    "TemporaryFailure",
]


# --- awsQuery ser/de ---
def to_query_text(value: BounceType) -> str:
    return value


def from_query_text(text: str) -> BounceType:
    return cast(BounceType, text)


def serialize_query(
    value: BounceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BounceType:
    return from_query_text(el.text or "")
