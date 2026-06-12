"""Generated from Smithy shape ``com.amazonaws.codebuild#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "CODECOMMIT",
    "CODEPIPELINE",
    "GITHUB",
    "GITLAB",
    "GITLAB_SELF_MANAGED",
    "S3",
    "BITBUCKET",
    "GITHUB_ENTERPRISE",
    "NO_SOURCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODECOMMIT",
        "CODEPIPELINE",
        "GITHUB",
        "GITLAB",
        "GITLAB_SELF_MANAGED",
        "S3",
        "BITBUCKET",
        "GITHUB_ENTERPRISE",
        "NO_SOURCE",
    )
)


def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {data!r}")
    return cast(SourceType, data)
