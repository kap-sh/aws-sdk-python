"""Generated from Smithy shape ``com.amazonaws.codebuild#ImagePullCredentialsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ImagePullCredentialsType: TypeAlias = Literal[
    "CODEBUILD",
    "SERVICE_ROLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODEBUILD",
        "SERVICE_ROLE",
    )
)


def serialize_aws_json_1_1(value: ImagePullCredentialsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImagePullCredentialsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImagePullCredentialsType value: {data!r}")
    return cast(ImagePullCredentialsType, data)
