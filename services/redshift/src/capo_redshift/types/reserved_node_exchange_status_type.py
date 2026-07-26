"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeExchangeStatusType``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

ReservedNodeExchangeStatusType: TypeAlias = Literal[
    "REQUESTED",
    "PENDING",
    "IN_PROGRESS",
    "RETRYING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsQuery ser/de ---
def to_query_text(value: ReservedNodeExchangeStatusType) -> str:
    return value


def from_query_text(text: str) -> ReservedNodeExchangeStatusType:
    return cast(ReservedNodeExchangeStatusType, text)


def serialize_query(
    value: ReservedNodeExchangeStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReservedNodeExchangeStatusType:
    return from_query_text(el.text or "")
