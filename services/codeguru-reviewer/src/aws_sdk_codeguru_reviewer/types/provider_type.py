"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ProviderType``."""

from typing import Literal, TypeAlias, cast

ProviderType: TypeAlias = Literal[
    "CodeCommit",
    "GitHub",
    "Bitbucket",
    "GitHubEnterpriseServer",
    "S3Bucket",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProviderType) -> str:
    return value


def deserialize_json(data: str) -> ProviderType:
    return cast(ProviderType, data)
