"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfEventActionEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.event_action_entry

ListOfEventActionEntry: TypeAlias = list[
    "aws_sdk_dataexchange.types.event_action_entry.EventActionEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfEventActionEntry) -> list:
    import aws_sdk_dataexchange.types.event_action_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_dataexchange.types.event_action_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfEventActionEntry:
    import aws_sdk_dataexchange.types.event_action_entry

    out: ListOfEventActionEntry = []
    for item in data:
        out.append(aws_sdk_dataexchange.types.event_action_entry.deserialize_json(item))
    return out
