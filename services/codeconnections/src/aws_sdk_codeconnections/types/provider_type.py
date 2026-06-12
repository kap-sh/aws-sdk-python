"""Generated from Smithy shape ``com.amazonaws.codeconnections#ProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeconnections.errors import DeserializationError

ProviderType: TypeAlias = Literal[
    "Bitbucket",
    "GitHub",
    "GitHubEnterpriseServer",
    "GitLab",
    "GitLabSelfManaged",
    "AzureDevOps",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Bitbucket",
        "GitHub",
        "GitHubEnterpriseServer",
        "GitLab",
        "GitLabSelfManaged",
        "AzureDevOps",
    )
)


def serialize_aws_json_1_0(value: ProviderType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProviderType value: {data!r}")
    return cast(ProviderType, data)
