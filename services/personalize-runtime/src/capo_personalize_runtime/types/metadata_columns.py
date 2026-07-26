"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#MetadataColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_runtime.types.column_names_list
    import capo_personalize_runtime.types.dataset_type

MetadataColumns: TypeAlias = dict[
    "capo_personalize_runtime.types.dataset_type.DatasetType",
    "capo_personalize_runtime.types.column_names_list.ColumnNamesList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MetadataColumns) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_personalize_runtime.types.column_names_list

        out[key] = capo_personalize_runtime.types.column_names_list.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> MetadataColumns:
    out: MetadataColumns = {}
    for key, value in data.items():
        import capo_personalize_runtime.types.column_names_list

        out[key] = capo_personalize_runtime.types.column_names_list.deserialize_json(
            value
        )
    return out
