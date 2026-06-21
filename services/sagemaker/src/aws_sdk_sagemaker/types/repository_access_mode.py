"""Generated from Smithy shape ``com.amazonaws.sagemaker#RepositoryAccessMode``."""

from typing import Literal, TypeAlias, cast

RepositoryAccessMode: TypeAlias = Literal[
    "Platform",
    "Vpc",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryAccessMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RepositoryAccessMode:
    return cast(RepositoryAccessMode, data)
