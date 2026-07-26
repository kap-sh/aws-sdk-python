"""Generated from Smithy shape ``com.amazonaws.qapps#CardValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.card_value

CardValueList: TypeAlias = list["capo_qapps.types.card_value.CardValue"]


# --- restJson1 ser/de ---
def serialize_json(value: CardValueList) -> list:
    import capo_qapps.types.card_value

    out: list = []
    for item in value:
        out.append(capo_qapps.types.card_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> CardValueList:
    import capo_qapps.types.card_value

    out: CardValueList = []
    for item in data:
        out.append(capo_qapps.types.card_value.deserialize_json(item))
    return out
