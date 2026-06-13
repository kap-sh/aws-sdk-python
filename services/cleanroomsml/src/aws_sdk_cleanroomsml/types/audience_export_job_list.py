"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceExportJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_export_job_summary

AudienceExportJobList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.audience_export_job_summary.AudienceExportJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceExportJobList) -> list:
    import aws_sdk_cleanroomsml.types.audience_export_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.audience_export_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AudienceExportJobList:
    import aws_sdk_cleanroomsml.types.audience_export_job_summary

    out: AudienceExportJobList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.audience_export_job_summary.deserialize_json(
                item
            )
        )
    return out
