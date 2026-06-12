"""Generated from Smithy shape ``com.amazonaws.codebuild#ServerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

ServerType: TypeAlias = Literal[
    "GITHUB",
    "BITBUCKET",
    "GITHUB_ENTERPRISE",
    "GITLAB",
    "GITLAB_SELF_MANAGED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GITHUB",
        "BITBUCKET",
        "GITHUB_ENTERPRISE",
        "GITLAB",
        "GITLAB_SELF_MANAGED",
    )
)


def serialize_aws_json_1_1(value: ServerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServerType value: {data!r}")
    return cast(ServerType, data)
