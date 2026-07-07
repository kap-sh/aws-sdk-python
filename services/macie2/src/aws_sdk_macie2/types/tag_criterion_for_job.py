"""Generated from Smithy shape ``com.amazonaws.macie2#TagCriterionForJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_tag_criterion_pair_for_job
    import aws_sdk_macie2.types.job_comparator


class TagCriterionForJob(TypedDict, closed=True):
    comparator: NotRequired["aws_sdk_macie2.types.job_comparator.JobComparator"]
    """<p>The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).</p>"""
    tag_values: NotRequired[
        "aws_sdk_macie2.types.__list_of_tag_criterion_pair_for_job.__listOfTagCriterionPairForJob"
    ]
    """<p>The tag keys, tag values, or tag key and value pairs to use in the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagCriterionForJob) -> dict:
    out: dict = {}
    if "comparator" in value:
        import aws_sdk_macie2.types.job_comparator

        out["comparator"] = aws_sdk_macie2.types.job_comparator.serialize_json(
            value["comparator"]
        )
    if "tag_values" in value:
        import aws_sdk_macie2.types.__list_of_tag_criterion_pair_for_job

        out["tagValues"] = (
            aws_sdk_macie2.types.__list_of_tag_criterion_pair_for_job.serialize_json(
                value["tag_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> TagCriterionForJob:
    out: TagCriterionForJob = {}  # type: ignore[typeddict-item]
    if "comparator" in data:
        import aws_sdk_macie2.types.job_comparator

        out["comparator"] = aws_sdk_macie2.types.job_comparator.deserialize_json(
            data["comparator"]
        )
    if "tagValues" in data:
        import aws_sdk_macie2.types.__list_of_tag_criterion_pair_for_job

        out["tag_values"] = (
            aws_sdk_macie2.types.__list_of_tag_criterion_pair_for_job.deserialize_json(
                data["tagValues"]
            )
        )
    return out
