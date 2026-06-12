"""Generated from Smithy shape ``com.amazonaws.qapps#CardStatusMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.card_status
    import aws_sdk_qapps.types.uuid

CardStatusMap: TypeAlias = dict[
    "aws_sdk_qapps.types.uuid.UUID", "aws_sdk_qapps.types.card_status.CardStatus"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CardStatusMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_qapps.types.card_status

        out[key] = aws_sdk_qapps.types.card_status.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CardStatusMap:
    out: CardStatusMap = {}
    for key, value in data.items():
        import aws_sdk_qapps.types.card_status

        out[key] = aws_sdk_qapps.types.card_status.deserialize_json(value)
    return out
