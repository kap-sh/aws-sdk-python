"""Generated from Smithy shape ``com.amazonaws.devopsagent#GitLabTokenType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of GitLab access token.</p>"""
GitLabTokenType: TypeAlias = Literal[
    "personal",
    "group",
]


# --- restJson1 ser/de ---
def serialize_json(value: GitLabTokenType) -> str:
    return value


def deserialize_json(data: str) -> GitLabTokenType:
    return cast(GitLabTokenType, data)
