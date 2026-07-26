"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeOfferingType``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

ReservedNodeOfferingType: TypeAlias = Literal[
    "Regular",
    "Upgradable",
]


# --- awsQuery ser/de ---
def to_query_text(value: ReservedNodeOfferingType) -> str:
    return value


def from_query_text(text: str) -> ReservedNodeOfferingType:
    return cast(ReservedNodeOfferingType, text)


def serialize_query(
    value: ReservedNodeOfferingType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ReservedNodeOfferingType:
    return from_query_text(el.text or "")
