"""Generated from Smithy shape ``com.amazonaws.backupsearch#Results``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backupsearch.types.result_item

Results: TypeAlias = list["capo_backupsearch.types.result_item.ResultItem"]


# --- restJson1 ser/de ---
def serialize_json(value: Results) -> list:
    import capo_backupsearch.types.result_item

    out: list = []
    for item in value:
        out.append(capo_backupsearch.types.result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> Results:
    import capo_backupsearch.types.result_item

    out: Results = []
    for item in data:
        out.append(capo_backupsearch.types.result_item.deserialize_json(item))
    return out
