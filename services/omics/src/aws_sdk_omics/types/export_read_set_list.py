"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.export_read_set

ExportReadSetList: TypeAlias = list["aws_sdk_omics.types.export_read_set.ExportReadSet"]


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetList) -> list:
    import aws_sdk_omics.types.export_read_set

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.export_read_set.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportReadSetList:
    import aws_sdk_omics.types.export_read_set

    out: ExportReadSetList = []
    for item in data:
        out.append(aws_sdk_omics.types.export_read_set.deserialize_json(item))
    return out
