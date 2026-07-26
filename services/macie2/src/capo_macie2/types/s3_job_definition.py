"""Generated from Smithy shape ``com.amazonaws.macie2#S3JobDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of_s3_bucket_definition_for_job
    import capo_macie2.types.s3_bucket_criteria_for_job
    import capo_macie2.types.scoping


class S3JobDefinition(TypedDict, closed=True):
    bucket_criteria: NotRequired[
        "capo_macie2.types.s3_bucket_criteria_for_job.S3BucketCriteriaForJob"
    ]
    """<p>The property- and tag-based conditions that determine which S3 buckets to include or exclude from the analysis. Each time the job runs, the job uses these criteria to determine which buckets contain objects to analyze. A job's definition can contain a bucketCriteria object or a bucketDefinitions array, not both.</p>"""
    bucket_definitions: NotRequired[
        "capo_macie2.types.__list_of_s3_bucket_definition_for_job.__listOfS3BucketDefinitionForJob"
    ]
    """<p>An array of objects, one for each Amazon Web Services account that owns specific S3 buckets to analyze. Each object specifies the account ID for an account and one or more buckets to analyze for that account. A job's definition can contain a bucketDefinitions array or a bucketCriteria object, not both.</p>"""
    scoping: NotRequired["capo_macie2.types.scoping.Scoping"]
    """<p>The property- and tag-based conditions that determine which S3 objects to include or exclude from the analysis. Each time the job runs, the job uses these criteria to determine which objects to analyze.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3JobDefinition) -> dict:
    out: dict = {}
    if "bucket_criteria" in value:
        import capo_macie2.types.s3_bucket_criteria_for_job

        out["bucketCriteria"] = (
            capo_macie2.types.s3_bucket_criteria_for_job.serialize_json(
                value["bucket_criteria"]
            )
        )
    if "bucket_definitions" in value:
        import capo_macie2.types.__list_of_s3_bucket_definition_for_job

        out["bucketDefinitions"] = (
            capo_macie2.types.__list_of_s3_bucket_definition_for_job.serialize_json(
                value["bucket_definitions"]
            )
        )
    if "scoping" in value:
        import capo_macie2.types.scoping

        out["scoping"] = capo_macie2.types.scoping.serialize_json(value["scoping"])
    return out


def deserialize_json(data: dict) -> S3JobDefinition:
    out: S3JobDefinition = {}  # type: ignore[typeddict-item]
    if "bucketCriteria" in data:
        import capo_macie2.types.s3_bucket_criteria_for_job

        out["bucket_criteria"] = (
            capo_macie2.types.s3_bucket_criteria_for_job.deserialize_json(
                data["bucketCriteria"]
            )
        )
    if "bucketDefinitions" in data:
        import capo_macie2.types.__list_of_s3_bucket_definition_for_job

        out["bucket_definitions"] = (
            capo_macie2.types.__list_of_s3_bucket_definition_for_job.deserialize_json(
                data["bucketDefinitions"]
            )
        )
    if "scoping" in data:
        import capo_macie2.types.scoping

        out["scoping"] = capo_macie2.types.scoping.deserialize_json(data["scoping"])
    return out
