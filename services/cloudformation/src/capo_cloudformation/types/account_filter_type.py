"""Generated from Smithy shape ``com.amazonaws.cloudformation#AccountFilterType``."""

from typing import Literal, TypeAlias, cast

from capo_cloudformation._protocol.xml import Element

AccountFilterType: TypeAlias = Literal[
    "NONE",
    "INTERSECTION",
    "DIFFERENCE",
    "UNION",
]


# --- awsQuery ser/de ---
def to_query_text(value: AccountFilterType) -> str:
    return value


def from_query_text(text: str) -> AccountFilterType:
    return cast(AccountFilterType, text)


def serialize_query(
    value: AccountFilterType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AccountFilterType:
    return from_query_text(el.text or "")
