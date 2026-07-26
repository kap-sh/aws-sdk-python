"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfDataGrantSummaryEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.data_grant_summary_entry

ListOfDataGrantSummaryEntry: TypeAlias = list[
    "capo_dataexchange.types.data_grant_summary_entry.DataGrantSummaryEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDataGrantSummaryEntry) -> list:
    import capo_dataexchange.types.data_grant_summary_entry

    out: list = []
    for item in value:
        out.append(
            capo_dataexchange.types.data_grant_summary_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfDataGrantSummaryEntry:
    import capo_dataexchange.types.data_grant_summary_entry

    out: ListOfDataGrantSummaryEntry = []
    for item in data:
        out.append(
            capo_dataexchange.types.data_grant_summary_entry.deserialize_json(item)
        )
    return out
