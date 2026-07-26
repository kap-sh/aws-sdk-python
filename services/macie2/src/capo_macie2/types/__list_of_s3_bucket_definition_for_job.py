"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfS3BucketDefinitionForJob``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.s3_bucket_definition_for_job

__listOfS3BucketDefinitionForJob: TypeAlias = list[
    "capo_macie2.types.s3_bucket_definition_for_job.S3BucketDefinitionForJob"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfS3BucketDefinitionForJob) -> list:
    import capo_macie2.types.s3_bucket_definition_for_job

    out: list = []
    for item in value:
        out.append(capo_macie2.types.s3_bucket_definition_for_job.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfS3BucketDefinitionForJob:
    import capo_macie2.types.s3_bucket_definition_for_job

    out: __listOfS3BucketDefinitionForJob = []
    for item in data:
        out.append(
            capo_macie2.types.s3_bucket_definition_for_job.deserialize_json(item)
        )
    return out
