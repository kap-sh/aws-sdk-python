"""Generated from Smithy shape ``com.amazonaws.connectcases#CustomFieldsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.custom_fields_filter

CustomFieldsFilterList: TypeAlias = list[
    "aws_sdk_connectcases.types.custom_fields_filter.CustomFieldsFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomFieldsFilterList) -> list:
    import aws_sdk_connectcases.types.custom_fields_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.custom_fields_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomFieldsFilterList:
    import aws_sdk_connectcases.types.custom_fields_filter

    out: CustomFieldsFilterList = []
    for item in data:
        out.append(
            aws_sdk_connectcases.types.custom_fields_filter.deserialize_json(item)
        )
    return out
