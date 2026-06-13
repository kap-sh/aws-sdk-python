"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportFileTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_export_file_type

TrainedModelExportFileTypeList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.trained_model_export_file_type.TrainedModelExportFileType"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportFileTypeList) -> list:
    import aws_sdk_cleanroomsml.types.trained_model_export_file_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.trained_model_export_file_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TrainedModelExportFileTypeList:
    import aws_sdk_cleanroomsml.types.trained_model_export_file_type

    out: TrainedModelExportFileTypeList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.trained_model_export_file_type.deserialize_json(
                item
            )
        )
    return out
