"""Generated from Smithy shape ``com.amazonaws.macie2#SimpleCriterionKeyForJob``."""

from typing import Literal, TypeAlias, cast

"""<p>The property to use in a condition that determines whether an S3 bucket is included or excluded from a classification job. Valid values are:</p>"""
SimpleCriterionKeyForJob: TypeAlias = Literal[
    "ACCOUNT_ID",
    "S3_BUCKET_NAME",
    "S3_BUCKET_EFFECTIVE_PERMISSION",
    "S3_BUCKET_SHARED_ACCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SimpleCriterionKeyForJob) -> str:
    return value


def deserialize_json(data: str) -> SimpleCriterionKeyForJob:
    return cast(SimpleCriterionKeyForJob, data)
