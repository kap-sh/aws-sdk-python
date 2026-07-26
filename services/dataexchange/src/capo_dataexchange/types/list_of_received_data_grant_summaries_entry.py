"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfReceivedDataGrantSummariesEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.received_data_grant_summaries_entry

ListOfReceivedDataGrantSummariesEntry: TypeAlias = list[
    "capo_dataexchange.types.received_data_grant_summaries_entry.ReceivedDataGrantSummariesEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfReceivedDataGrantSummariesEntry) -> list:
    import capo_dataexchange.types.received_data_grant_summaries_entry

    out: list = []
    for item in value:
        out.append(
            capo_dataexchange.types.received_data_grant_summaries_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOfReceivedDataGrantSummariesEntry:
    import capo_dataexchange.types.received_data_grant_summaries_entry

    out: ListOfReceivedDataGrantSummariesEntry = []
    for item in data:
        out.append(
            capo_dataexchange.types.received_data_grant_summaries_entry.deserialize_json(
                item
            )
        )
    return out
