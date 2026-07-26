"""Generated from Smithy shape ``com.amazonaws.qapps#CardList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.card_input

CardList: TypeAlias = list["capo_qapps.types.card_input.CardInput"]


# --- restJson1 ser/de ---
def serialize_json(value: CardList) -> list:
    import capo_qapps.types.card_input

    out: list = []
    for item in value:
        out.append(capo_qapps.types.card_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> CardList:
    import capo_qapps.types.card_input

    out: CardList = []
    for item in data:
        out.append(capo_qapps.types.card_input.deserialize_json(item))
    return out
