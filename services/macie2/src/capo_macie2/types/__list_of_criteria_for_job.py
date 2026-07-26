"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfCriteriaForJob``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.criteria_for_job

__listOfCriteriaForJob: TypeAlias = list[
    "capo_macie2.types.criteria_for_job.CriteriaForJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCriteriaForJob) -> list:
    import capo_macie2.types.criteria_for_job

    out: list = []
    for item in value:
        out.append(capo_macie2.types.criteria_for_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCriteriaForJob:
    import capo_macie2.types.criteria_for_job

    out: __listOfCriteriaForJob = []
    for item in data:
        out.append(capo_macie2.types.criteria_for_job.deserialize_json(item))
    return out
