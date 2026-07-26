"""Generated from Smithy shape ``com.amazonaws.qbusiness#Messages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.message

Messages: TypeAlias = list["capo_qbusiness.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: Messages) -> list:
    import capo_qbusiness.types.message

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.message.serialize_json(item))
    return out


def deserialize_json(data: list) -> Messages:
    import capo_qbusiness.types.message

    out: Messages = []
    for item in data:
        out.append(capo_qbusiness.types.message.deserialize_json(item))
    return out
