"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfCriteriaForJob``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.criteria_for_job

__listOfCriteriaForJob: TypeAlias = list[
    "aws_sdk_macie2.types.criteria_for_job.CriteriaForJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCriteriaForJob) -> list:
    import aws_sdk_macie2.types.criteria_for_job

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.criteria_for_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCriteriaForJob:
    import aws_sdk_macie2.types.criteria_for_job

    out: __listOfCriteriaForJob = []
    for item in data:
        out.append(aws_sdk_macie2.types.criteria_for_job.deserialize_json(item))
    return out
