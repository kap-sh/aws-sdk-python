"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldFolder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_folder_description
    import capo_quicksight.types.folder_column_list


class FieldFolder(TypedDict, closed=True):
    description: NotRequired[
        "capo_quicksight.types.field_folder_description.FieldFolderDescription"
    ]
    """<p>The description for a field folder.</p>"""
    columns: NotRequired["capo_quicksight.types.folder_column_list.FolderColumnList"]
    """<p>A folder has a list of columns. A column can only be in one folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldFolder) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "columns" in value:
        import capo_quicksight.types.folder_column_list

        out["columns"] = capo_quicksight.types.folder_column_list.serialize_json(
            value["columns"]
        )
    return out


def deserialize_json(data: dict) -> FieldFolder:
    out: FieldFolder = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "columns" in data:
        import capo_quicksight.types.folder_column_list

        out["columns"] = capo_quicksight.types.folder_column_list.deserialize_json(
            data["columns"]
        )
    return out
