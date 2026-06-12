"""Generated from Smithy shape ``com.amazonaws.macie2#GroupBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

GroupBy: TypeAlias = Literal[
    "resourcesAffected.s3Bucket.name",
    "type",
    "classificationDetails.jobId",
    "severity.description",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "resourcesAffected.s3Bucket.name",
        "type",
        "classificationDetails.jobId",
        "severity.description",
    )
)


def serialize_json(value: GroupBy) -> str:
    return value


def deserialize_json(data: str) -> GroupBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupBy value: {data!r}")
    return cast(GroupBy, data)
