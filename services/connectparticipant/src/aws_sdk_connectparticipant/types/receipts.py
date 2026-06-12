"""Generated from Smithy shape ``com.amazonaws.connectparticipant#Receipts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.receipt

Receipts: TypeAlias = list["aws_sdk_connectparticipant.types.receipt.Receipt"]


# --- restJson1 ser/de ---
def serialize_json(value: Receipts) -> list:
    import aws_sdk_connectparticipant.types.receipt

    out: list = []
    for item in value:
        out.append(aws_sdk_connectparticipant.types.receipt.serialize_json(item))
    return out


def deserialize_json(data: list) -> Receipts:
    import aws_sdk_connectparticipant.types.receipt

    out: Receipts = []
    for item in data:
        out.append(aws_sdk_connectparticipant.types.receipt.deserialize_json(item))
    return out
