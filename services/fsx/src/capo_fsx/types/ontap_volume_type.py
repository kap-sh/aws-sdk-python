"""Generated from Smithy shape ``com.amazonaws.fsx#OntapVolumeType``."""

from typing import Literal, TypeAlias, cast

OntapVolumeType: TypeAlias = Literal[
    "RW",
    "DP",
    "LS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OntapVolumeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OntapVolumeType:
    return cast(OntapVolumeType, data)
