"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_connections.errors import DeserializationError

ProviderType: TypeAlias = Literal[
    "Bitbucket",
    "GitHub",
    "GitHubEnterpriseServer",
    "GitLab",
    "GitLabSelfManaged",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Bitbucket",
        "GitHub",
        "GitHubEnterpriseServer",
        "GitLab",
        "GitLabSelfManaged",
    )
)


def serialize_aws_json_1_0(value: ProviderType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProviderType value: {data!r}")
    return cast(ProviderType, data)
