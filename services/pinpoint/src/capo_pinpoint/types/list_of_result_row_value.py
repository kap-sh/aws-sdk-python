"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfResultRowValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.result_row_value

ListOfResultRowValue: TypeAlias = list[
    "capo_pinpoint.types.result_row_value.ResultRowValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfResultRowValue) -> list:
    import capo_pinpoint.types.result_row_value

    out: list = []
    for item in value:
        out.append(capo_pinpoint.types.result_row_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfResultRowValue:
    import capo_pinpoint.types.result_row_value

    out: ListOfResultRowValue = []
    for item in data:
        out.append(capo_pinpoint.types.result_row_value.deserialize_json(item))
    return out
