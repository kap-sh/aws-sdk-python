"""Generated from Smithy shape ``com.amazonaws.codebuild#ArtifactPackaging``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ArtifactPackaging: TypeAlias = Literal[
    "NONE",
    "ZIP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ZIP",
    )
)


def serialize_aws_json_1_1(value: ArtifactPackaging) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactPackaging:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactPackaging value: {data!r}")
    return cast(ArtifactPackaging, data)
