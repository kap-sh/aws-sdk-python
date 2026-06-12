"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactLocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ArtifactLocationType: TypeAlias = Literal["S3",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3",))


def serialize_aws_json_1_1(value: ArtifactLocationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactLocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactLocationType value: {data!r}")
    return cast(ArtifactLocationType, data)
