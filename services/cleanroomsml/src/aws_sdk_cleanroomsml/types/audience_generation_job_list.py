"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceGenerationJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_generation_job_summary

AudienceGenerationJobList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.audience_generation_job_summary.AudienceGenerationJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceGenerationJobList) -> list:
    import aws_sdk_cleanroomsml.types.audience_generation_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.audience_generation_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AudienceGenerationJobList:
    import aws_sdk_cleanroomsml.types.audience_generation_job_summary

    out: AudienceGenerationJobList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.audience_generation_job_summary.deserialize_json(
                item
            )
        )
    return out
