"""Generated from Smithy shape ``com.amazonaws.qapps#CardValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_value

CardValueList: TypeAlias = list["aws_sdk_qapps.types.card_value.CardValue"]


# --- restJson1 ser/de ---
def serialize_json(value: CardValueList) -> list:
    import aws_sdk_qapps.types.card_value

    out: list = []
    for item in value:
        out.append(aws_sdk_qapps.types.card_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> CardValueList:
    import aws_sdk_qapps.types.card_value

    out: CardValueList = []
    for item in data:
        out.append(aws_sdk_qapps.types.card_value.deserialize_json(item))
    return out
