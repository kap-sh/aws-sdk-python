"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListImportFileTaskInformation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.import_file_task_information

ListImportFileTaskInformation: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.import_file_task_information.ImportFileTaskInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListImportFileTaskInformation) -> list:
    import aws_sdk_migrationhubstrategy.types.import_file_task_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.import_file_task_information.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListImportFileTaskInformation:
    import aws_sdk_migrationhubstrategy.types.import_file_task_information

    out: ListImportFileTaskInformation = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.import_file_task_information.deserialize_json(
                item
            )
        )
    return out
