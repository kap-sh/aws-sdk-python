"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfMessageHeader``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.message_header

ListOfMessageHeader: TypeAlias = list[
    "capo_pinpoint.types.message_header.MessageHeader"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfMessageHeader) -> list:
    import capo_pinpoint.types.message_header

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.message_header.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfMessageHeader:
    import capo_pinpoint.types.message_header

    out: ListOfMessageHeader = []
    for item in data:
        out.append(capo_pinpoint.types.message_header.deserialize_json(item))
    return out
