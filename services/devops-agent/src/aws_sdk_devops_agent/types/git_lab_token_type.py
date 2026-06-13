"""Generated from Smithy shape ``com.amazonaws.devopsagent#GitLabTokenType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Type of GitLab access token.</p>"""
GitLabTokenType: TypeAlias = Literal[
    "personal",
    "group",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "personal",
        "group",
    )
)


def serialize_json(value: GitLabTokenType) -> str:
    return value


def deserialize_json(data: str) -> GitLabTokenType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GitLabTokenType value: {data!r}")
    return cast(GitLabTokenType, data)
