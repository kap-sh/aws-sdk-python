"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfTagCriterionPairForJob``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_macie2.types.tag_criterion_pair_for_job

__listOfTagCriterionPairForJob: TypeAlias = list[
    "aws_sdk_macie2.types.tag_criterion_pair_for_job.TagCriterionPairForJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfTagCriterionPairForJob) -> list:
    import aws_sdk_macie2.types.tag_criterion_pair_for_job

    out: list = []
    for item in value:
        out.append(aws_sdk_macie2.types.tag_criterion_pair_for_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfTagCriterionPairForJob:
    import aws_sdk_macie2.types.tag_criterion_pair_for_job

    out: __listOfTagCriterionPairForJob = []
    for item in data:
        out.append(
            aws_sdk_macie2.types.tag_criterion_pair_for_job.deserialize_json(item)
        )
    return out
