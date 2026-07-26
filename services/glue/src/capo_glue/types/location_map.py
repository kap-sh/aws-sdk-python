"""Generated from Smithy shape ``com.amazonaws.glue#LocationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.column_values_string

LocationMap: TypeAlias = dict[
    "capo_glue.types.column_values_string.ColumnValuesString",
    "capo_glue.types.column_values_string.ColumnValuesString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LocationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationMap:
    out: LocationMap = {}
    for key, value in data.items():
        out[key] = value
    return out
