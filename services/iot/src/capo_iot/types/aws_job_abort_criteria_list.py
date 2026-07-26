"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.aws_job_abort_criteria

AwsJobAbortCriteriaList: TypeAlias = list[
    "capo_iot.types.aws_job_abort_criteria.AwsJobAbortCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobAbortCriteriaList) -> list:
    import capo_iot.types.aws_job_abort_criteria

    out: list = []
    for item in value:
        out.append(capo_iot.types.aws_job_abort_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsJobAbortCriteriaList:
    import capo_iot.types.aws_job_abort_criteria

    out: AwsJobAbortCriteriaList = []
    for item in data:
        out.append(capo_iot.types.aws_job_abort_criteria.deserialize_json(item))
    return out
