"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionKeyType``."""

from typing import Literal, TypeAlias, cast

MultiRegionKeyType: TypeAlias = Literal[
    "PRIMARY",
    "REPLICA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionKeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MultiRegionKeyType:
    return cast(MultiRegionKeyType, data)
