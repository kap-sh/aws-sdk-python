"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomFieldsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.custom_fields_filter

CustomFieldsFilterList: TypeAlias = list[
    "capo_connectcases.types.custom_fields_filter.CustomFieldsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomFieldsFilterList) -> list:
    import capo_connectcases.types.custom_fields_filter

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.custom_fields_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomFieldsFilterList:
    import capo_connectcases.types.custom_fields_filter

    out: CustomFieldsFilterList = []
    for item in data:
        out.append(capo_connectcases.types.custom_fields_filter.deserialize_json(item))
    return out
