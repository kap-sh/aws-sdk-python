"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#Metadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.column_name
    import aws_sdk_personalize_runtime.types.column_value

Metadata: TypeAlias = dict[
    "aws_sdk_personalize_runtime.types.column_name.ColumnName",
    "aws_sdk_personalize_runtime.types.column_value.ColumnValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Metadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Metadata:
    out: Metadata = {}
    for key, value in data.items():
        out[key] = value
    return out
