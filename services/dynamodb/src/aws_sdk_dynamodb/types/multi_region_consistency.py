"""Generated from Smithy shape ``com.amazonaws.dynamodb#MultiRegionConsistency``."""

from typing import Literal, TypeAlias, cast

MultiRegionConsistency: TypeAlias = Literal[
    "EVENTUAL",
    "STRONG",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultiRegionConsistency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MultiRegionConsistency:
    return cast(MultiRegionConsistency, data)
