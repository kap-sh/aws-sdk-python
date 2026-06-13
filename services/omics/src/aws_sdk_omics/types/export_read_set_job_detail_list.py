"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetJobDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.export_read_set_job_detail

ExportReadSetJobDetailList: TypeAlias = list[
    "aws_sdk_omics.types.export_read_set_job_detail.ExportReadSetJobDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetJobDetailList) -> list:
    import aws_sdk_omics.types.export_read_set_job_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.export_read_set_job_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportReadSetJobDetailList:
    import aws_sdk_omics.types.export_read_set_job_detail

    out: ExportReadSetJobDetailList = []
    for item in data:
        out.append(
            aws_sdk_omics.types.export_read_set_job_detail.deserialize_json(item)
        )
    return out
