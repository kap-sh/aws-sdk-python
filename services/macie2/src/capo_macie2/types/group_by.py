"""Generated from Smithy shape ``com.amazonaws.macie2#GroupBy``."""

from typing import Literal, TypeAlias, cast

GroupBy: TypeAlias = Literal[
    "resourcesAffected.s3Bucket.name",
    "type",
    "classificationDetails.jobId",
    "severity.description",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupBy) -> str:
    return value


def deserialize_json(data: str) -> GroupBy:
    return cast(GroupBy, data)
