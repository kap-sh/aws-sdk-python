"""Generated from Smithy shape ``com.amazonaws.omics#RunExportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.run_export

RunExportList: TypeAlias = list["aws_sdk_omics.types.run_export.RunExport"]


# --- restJson1 ser/de ---
def serialize_json(value: RunExportList) -> list:
    return list(value)


def deserialize_json(data: list) -> RunExportList:
    return list(data)
