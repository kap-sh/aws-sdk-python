"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfDataSetEntry``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.data_set_entry

ListOfDataSetEntry: TypeAlias = list[
    "capo_dataexchange.types.data_set_entry.DataSetEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfDataSetEntry) -> list:
    import capo_dataexchange.types.data_set_entry

    out: list = []
    for item in value:
        out.append(capo_dataexchange.types.data_set_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfDataSetEntry:
    import capo_dataexchange.types.data_set_entry

    out: ListOfDataSetEntry = []
    for item in data:
        out.append(capo_dataexchange.types.data_set_entry.deserialize_json(item))
    return out
