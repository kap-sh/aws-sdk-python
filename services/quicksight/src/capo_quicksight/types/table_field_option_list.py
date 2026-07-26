"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.table_field_option

TableFieldOptionList: TypeAlias = list[
    "capo_quicksight.types.table_field_option.TableFieldOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldOptionList) -> list:
    import capo_quicksight.types.table_field_option

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.table_field_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableFieldOptionList:
    import capo_quicksight.types.table_field_option

    out: TableFieldOptionList = []
    for item in data:
        out.append(capo_quicksight.types.table_field_option.deserialize_json(item))
    return out
