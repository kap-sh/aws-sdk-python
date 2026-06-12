"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IncludedColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.column_names_list

IncludedColumns: TypeAlias = dict[
    "str", "aws_sdk_customer_profiles.types.column_names_list.ColumnNamesList"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: IncludedColumns) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_customer_profiles.types.column_names_list

        out[key] = aws_sdk_customer_profiles.types.column_names_list.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> IncludedColumns:
    out: IncludedColumns = {}
    for key, value in data.items():
        import aws_sdk_customer_profiles.types.column_names_list

        out[key] = aws_sdk_customer_profiles.types.column_names_list.deserialize_json(
            value
        )
    return out
