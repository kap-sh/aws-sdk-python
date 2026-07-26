"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldFolderMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.field_folder
    import capo_quicksight.types.field_folder_path

FieldFolderMap: TypeAlias = dict[
    "capo_quicksight.types.field_folder_path.FieldFolderPath",
    "capo_quicksight.types.field_folder.FieldFolder",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FieldFolderMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_quicksight.types.field_folder

        out[key] = capo_quicksight.types.field_folder.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FieldFolderMap:
    out: FieldFolderMap = {}
    for key, value in data.items():
        import capo_quicksight.types.field_folder

        out[key] = capo_quicksight.types.field_folder.deserialize_json(value)
    return out
