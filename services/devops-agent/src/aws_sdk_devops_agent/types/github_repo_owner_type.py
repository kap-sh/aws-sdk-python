"""Generated from Smithy shape ``com.amazonaws.devopsagent#GithubRepoOwnerType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of GitHub repository owner.</p>"""
GithubRepoOwnerType: TypeAlias = Literal[
    "organization",
    "user",
]


# --- restJson1 ser/de ---
def serialize_json(value: GithubRepoOwnerType) -> str:
    return value


def deserialize_json(data: str) -> GithubRepoOwnerType:
    return cast(GithubRepoOwnerType, data)
