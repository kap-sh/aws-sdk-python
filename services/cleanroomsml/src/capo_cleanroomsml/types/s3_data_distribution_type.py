"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#S3DataDistributionType``."""

from typing import Literal, TypeAlias, cast

S3DataDistributionType: TypeAlias = Literal[
    "FullyReplicated",
    "ShardedByS3Key",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3DataDistributionType) -> str:
    return value


def deserialize_json(data: str) -> S3DataDistributionType:
    return cast(S3DataDistributionType, data)
