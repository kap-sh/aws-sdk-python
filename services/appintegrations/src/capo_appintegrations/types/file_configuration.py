"""Generated from Smithy shape ``com.amazonaws.appintegrations#FileConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appintegrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appintegrations.types.fields_map
    import capo_appintegrations.types.folder_list


class FileConfiguration(TypedDict, closed=True):
    folders: "capo_appintegrations.types.folder_list.FolderList"
    """<p>Identifiers for the source folders to pull all files from recursively.</p>"""
    filters: NotRequired["capo_appintegrations.types.fields_map.FieldsMap"]
    """<p>Restrictions for what files should be pulled from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileConfiguration) -> dict:
    out: dict = {}
    import capo_appintegrations.types.folder_list

    out["Folders"] = capo_appintegrations.types.folder_list.serialize_json(
        value["folders"]
    )
    if "filters" in value:
        import capo_appintegrations.types.fields_map

        out["Filters"] = capo_appintegrations.types.fields_map.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> FileConfiguration:
    out: FileConfiguration = {}  # type: ignore[typeddict-item]
    if "Folders" in data:
        import capo_appintegrations.types.folder_list

        out["folders"] = capo_appintegrations.types.folder_list.deserialize_json(
            data["Folders"]
        )
    else:
        raise DeserializationError("FileConfiguration.folders required")
    if "Filters" in data:
        import capo_appintegrations.types.fields_map

        out["filters"] = capo_appintegrations.types.fields_map.deserialize_json(
            data["Filters"]
        )
    return out
