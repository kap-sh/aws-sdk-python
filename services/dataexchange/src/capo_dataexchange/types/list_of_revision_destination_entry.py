"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfRevisionDestinationEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.revision_destination_entry

ListOfRevisionDestinationEntry: TypeAlias = list[
    "capo_dataexchange.types.revision_destination_entry.RevisionDestinationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRevisionDestinationEntry) -> list:
    import capo_dataexchange.types.revision_destination_entry

    out: list = []
    for item in value:
        out.append(
            capo_dataexchange.types.revision_destination_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfRevisionDestinationEntry:
    import capo_dataexchange.types.revision_destination_entry

    out: ListOfRevisionDestinationEntry = []
    for item in data:
        out.append(
            capo_dataexchange.types.revision_destination_entry.deserialize_json(item)
        )
    return out
