"""Generated from Smithy shape ``com.amazonaws.codebuild#ArtifactNamespace``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ArtifactNamespace: TypeAlias = Literal[
    "NONE",
    "BUILD_ID",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "BUILD_ID",
    )
)


def serialize_aws_json_1_1(value: ArtifactNamespace) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ArtifactNamespace:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArtifactNamespace value: {data!r}")
    return cast(ArtifactNamespace, data)
