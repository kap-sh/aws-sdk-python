"""Generated from Smithy shape ``com.amazonaws.macie2#S3BucketCriteriaForJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.criteria_block_for_job


class S3BucketCriteriaForJob(TypedDict):
    excludes: NotRequired[
        "aws_sdk_macie2.types.criteria_block_for_job.CriteriaBlockForJob"
    ]
    """<p>The property- and tag-based conditions that determine which buckets to exclude from the job.</p>"""
    includes: NotRequired[
        "aws_sdk_macie2.types.criteria_block_for_job.CriteriaBlockForJob"
    ]
    """<p>The property- and tag-based conditions that determine which buckets to include in the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketCriteriaForJob) -> dict:
    out: dict = {}
    if "excludes" in value:
        import aws_sdk_macie2.types.criteria_block_for_job

        out["excludes"] = aws_sdk_macie2.types.criteria_block_for_job.serialize_json(
            value["excludes"]
        )
    if "includes" in value:
        import aws_sdk_macie2.types.criteria_block_for_job

        out["includes"] = aws_sdk_macie2.types.criteria_block_for_job.serialize_json(
            value["includes"]
        )
    return out


def deserialize_json(data: dict) -> S3BucketCriteriaForJob:
    out: S3BucketCriteriaForJob = {}  # type: ignore[typeddict-item]
    if "excludes" in data:
        import aws_sdk_macie2.types.criteria_block_for_job

        out["excludes"] = aws_sdk_macie2.types.criteria_block_for_job.deserialize_json(
            data["excludes"]
        )
    if "includes" in data:
        import aws_sdk_macie2.types.criteria_block_for_job

        out["includes"] = aws_sdk_macie2.types.criteria_block_for_job.deserialize_json(
            data["includes"]
        )
    return out
