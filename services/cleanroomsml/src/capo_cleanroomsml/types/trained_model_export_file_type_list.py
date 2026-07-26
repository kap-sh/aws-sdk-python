"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportFileTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_export_file_type

TrainedModelExportFileTypeList: TypeAlias = list[
    "capo_cleanroomsml.types.trained_model_export_file_type.TrainedModelExportFileType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportFileTypeList) -> list:
    import capo_cleanroomsml.types.trained_model_export_file_type

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.trained_model_export_file_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TrainedModelExportFileTypeList:
    import capo_cleanroomsml.types.trained_model_export_file_type

    out: TrainedModelExportFileTypeList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.trained_model_export_file_type.deserialize_json(
                item
            )
        )
    return out
