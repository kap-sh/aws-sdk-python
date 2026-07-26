"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceGenerationJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_generation_job_summary

AudienceGenerationJobList: TypeAlias = list[
    "capo_cleanroomsml.types.audience_generation_job_summary.AudienceGenerationJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceGenerationJobList) -> list:
    import capo_cleanroomsml.types.audience_generation_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.audience_generation_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AudienceGenerationJobList:
    import capo_cleanroomsml.types.audience_generation_job_summary

    out: AudienceGenerationJobList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.audience_generation_job_summary.deserialize_json(
                item
            )
        )
    return out
