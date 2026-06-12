"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#MetadataColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.column_names_list
    import aws_sdk_personalize_runtime.types.dataset_type

MetadataColumns: TypeAlias = dict[
    "aws_sdk_personalize_runtime.types.dataset_type.DatasetType",
    "aws_sdk_personalize_runtime.types.column_names_list.ColumnNamesList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MetadataColumns) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_personalize_runtime.types.column_names_list

        out[key] = aws_sdk_personalize_runtime.types.column_names_list.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> MetadataColumns:
    out: MetadataColumns = {}
    for key, value in data.items():
        import aws_sdk_personalize_runtime.types.column_names_list

        out[key] = aws_sdk_personalize_runtime.types.column_names_list.deserialize_json(
            value
        )
    return out
