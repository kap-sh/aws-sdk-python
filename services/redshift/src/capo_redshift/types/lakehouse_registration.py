"""Generated from Smithy shape ``com.amazonaws.redshift#LakehouseRegistration``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

LakehouseRegistration: TypeAlias = Literal[
    "Register",
    "Deregister",
]


# --- awsQuery ser/de ---
def to_query_text(value: LakehouseRegistration) -> str:
    return value


def from_query_text(text: str) -> LakehouseRegistration:
    return cast(LakehouseRegistration, text)


def serialize_query(
    value: LakehouseRegistration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LakehouseRegistration:
    return from_query_text(el.text or "")
