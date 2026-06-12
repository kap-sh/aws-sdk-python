"""Generated from Smithy shape ``com.amazonaws.qapps#CardModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card

CardModelList: TypeAlias = list["aws_sdk_qapps.types.card.Card"]


# --- restJson1 ser/de ---
def serialize_json(value: CardModelList) -> list:
    import aws_sdk_qapps.types.card

    out: list = []
    for item in value:
        out.append(aws_sdk_qapps.types.card.serialize_json(item))
    return out


def deserialize_json(data: list) -> CardModelList:
    import aws_sdk_qapps.types.card

    out: CardModelList = []
    for item in data:
        out.append(aws_sdk_qapps.types.card.deserialize_json(item))
    return out
