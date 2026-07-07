"""Generated from Smithy shape ``com.amazonaws.macie2#CriteriaForJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.simple_criterion_for_job
    import aws_sdk_macie2.types.tag_criterion_for_job


class CriteriaForJob(TypedDict, closed=True):
    simple_criterion: NotRequired[
        "aws_sdk_macie2.types.simple_criterion_for_job.SimpleCriterionForJob"
    ]
    """<p>A property-based condition that defines a property, operator, and one or more values for including or excluding buckets from the job.</p>"""
    tag_criterion: NotRequired[
        "aws_sdk_macie2.types.tag_criterion_for_job.TagCriterionForJob"
    ]
    """<p>A tag-based condition that defines an operator and tag keys, tag values, or tag key and value pairs for including or excluding buckets from the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CriteriaForJob) -> dict:
    out: dict = {}
    if "simple_criterion" in value:
        import aws_sdk_macie2.types.simple_criterion_for_job

        out["simpleCriterion"] = (
            aws_sdk_macie2.types.simple_criterion_for_job.serialize_json(
                value["simple_criterion"]
            )
        )
    if "tag_criterion" in value:
        import aws_sdk_macie2.types.tag_criterion_for_job

        out["tagCriterion"] = aws_sdk_macie2.types.tag_criterion_for_job.serialize_json(
            value["tag_criterion"]
        )
    return out


def deserialize_json(data: dict) -> CriteriaForJob:
    out: CriteriaForJob = {}  # type: ignore[typeddict-item]
    if "simpleCriterion" in data:
        import aws_sdk_macie2.types.simple_criterion_for_job

        out["simple_criterion"] = (
            aws_sdk_macie2.types.simple_criterion_for_job.deserialize_json(
                data["simpleCriterion"]
            )
        )
    if "tagCriterion" in data:
        import aws_sdk_macie2.types.tag_criterion_for_job

        out["tag_criterion"] = (
            aws_sdk_macie2.types.tag_criterion_for_job.deserialize_json(
                data["tagCriterion"]
            )
        )
    return out
