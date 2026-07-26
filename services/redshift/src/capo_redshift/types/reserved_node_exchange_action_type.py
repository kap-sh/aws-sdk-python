"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeExchangeActionType``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

ReservedNodeExchangeActionType: TypeAlias = Literal[
    "restore-cluster",
    "resize-cluster",
]


# --- awsQuery ser/de ---
def to_query_text(value: ReservedNodeExchangeActionType) -> str:
    return value


def from_query_text(text: str) -> ReservedNodeExchangeActionType:
    return cast(ReservedNodeExchangeActionType, text)


def serialize_query(
    value: ReservedNodeExchangeActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReservedNodeExchangeActionType:
    return from_query_text(el.text or "")
