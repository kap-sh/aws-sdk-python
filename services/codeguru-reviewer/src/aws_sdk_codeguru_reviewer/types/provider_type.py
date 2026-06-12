"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

ProviderType: TypeAlias = Literal[
    "CodeCommit",
    "GitHub",
    "Bitbucket",
    "GitHubEnterpriseServer",
    "S3Bucket",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CodeCommit",
        "GitHub",
        "Bitbucket",
        "GitHubEnterpriseServer",
        "S3Bucket",
    )
)


def serialize_json(value: ProviderType) -> str:
    return value


def deserialize_json(data: str) -> ProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProviderType value: {data!r}")
    return cast(ProviderType, data)
