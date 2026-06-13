"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetImportJobSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.start_read_set_import_job_source_item

StartReadSetImportJobSourceList: TypeAlias = list[
    "aws_sdk_omics.types.start_read_set_import_job_source_item.StartReadSetImportJobSourceItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetImportJobSourceList) -> list:
    import aws_sdk_omics.types.start_read_set_import_job_source_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_omics.types.start_read_set_import_job_source_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StartReadSetImportJobSourceList:
    import aws_sdk_omics.types.start_read_set_import_job_source_item

    out: StartReadSetImportJobSourceList = []
    for item in data:
        out.append(
            aws_sdk_omics.types.start_read_set_import_job_source_item.deserialize_json(
                item
            )
        )
    return out
