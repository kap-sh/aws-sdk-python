"""Generated from Smithy shape ``com.amazonaws.fsx#InputOntapVolumeType``."""

from typing import Literal, TypeAlias, cast

InputOntapVolumeType: TypeAlias = Literal[
    "RW",
    "DP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputOntapVolumeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputOntapVolumeType:
    return cast(InputOntapVolumeType, data)
