"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfDataGrantSummaryEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.data_grant_summary_entry

ListOfDataGrantSummaryEntry: TypeAlias = list[
    "aws_sdk_dataexchange.types.data_grant_summary_entry.DataGrantSummaryEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDataGrantSummaryEntry) -> list:
    import aws_sdk_dataexchange.types.data_grant_summary_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dataexchange.types.data_grant_summary_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfDataGrantSummaryEntry:
    import aws_sdk_dataexchange.types.data_grant_summary_entry

    out: ListOfDataGrantSummaryEntry = []
    for item in data:
        out.append(
            aws_sdk_dataexchange.types.data_grant_summary_entry.deserialize_json(item)
        )
    return out
