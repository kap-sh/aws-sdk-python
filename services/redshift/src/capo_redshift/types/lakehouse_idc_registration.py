"""Generated from Smithy shape ``com.amazonaws.redshift#LakehouseIdcRegistration``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

LakehouseIdcRegistration: TypeAlias = Literal[
    "Associate",
    "Disassociate",
]


# --- awsQuery ser/de ---
def to_query_text(value: LakehouseIdcRegistration) -> str:
    return value


def from_query_text(text: str) -> LakehouseIdcRegistration:
    return cast(LakehouseIdcRegistration, text)


def serialize_query(
    value: LakehouseIdcRegistration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LakehouseIdcRegistration:
    return from_query_text(el.text or "")
