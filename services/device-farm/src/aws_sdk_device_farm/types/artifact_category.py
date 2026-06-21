"""Generated from Smithy shape ``com.amazonaws.devicefarm#ArtifactCategory``."""

from typing import Literal, TypeAlias, cast

ArtifactCategory: TypeAlias = Literal[
    "SCREENSHOT",
    "FILE",
    "LOG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactCategory:
    return cast(ArtifactCategory, data)
