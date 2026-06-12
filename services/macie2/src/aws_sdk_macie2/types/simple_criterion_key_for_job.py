"""Generated from Smithy shape ``com.amazonaws.macie2#SimpleCriterionKeyForJob``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The property to use in a condition that determines whether an S3 bucket is included or excluded from a classification job. Valid values are:</p>"""
SimpleCriterionKeyForJob: TypeAlias = Literal[
    "ACCOUNT_ID",
    "S3_BUCKET_NAME",
    "S3_BUCKET_EFFECTIVE_PERMISSION",
    "S3_BUCKET_SHARED_ACCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_ID",
        "S3_BUCKET_NAME",
        "S3_BUCKET_EFFECTIVE_PERMISSION",
        "S3_BUCKET_SHARED_ACCESS",
    )
)


def serialize_json(value: SimpleCriterionKeyForJob) -> str:
    return value


def deserialize_json(data: str) -> SimpleCriterionKeyForJob:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SimpleCriterionKeyForJob value: {data!r}")
    return cast(SimpleCriterionKeyForJob, data)
