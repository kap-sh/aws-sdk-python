"""Generated from Smithy shape ``com.amazonaws.codebuild#ArtifactsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ArtifactsType: TypeAlias = Literal[
    "CODEPIPELINE",
    "S3",
    "NO_ARTIFACTS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODEPIPELINE",
        "S3",
        "NO_ARTIFACTS",
    )
)


def serialize_aws_json_1_1(value: ArtifactsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactsType value: {data!r}")
    return cast(ArtifactsType, data)
