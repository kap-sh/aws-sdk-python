"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfResultRow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.result_row

ListOfResultRow: TypeAlias = list["capo_pinpoint.types.result_row.ResultRow"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfResultRow) -> list:
    import capo_pinpoint.types.result_row

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.result_row.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfResultRow:
    import capo_pinpoint.types.result_row

    out: ListOfResultRow = []
    for item in data:
        out.append(capo_pinpoint.types.result_row.deserialize_json(item))
    return out
