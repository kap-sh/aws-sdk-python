"""Generated from Smithy shape ``com.amazonaws.devopsagent#GithubRepoOwnerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Type of GitHub repository owner.</p>"""
GithubRepoOwnerType: TypeAlias = Literal[
    "organization",
    "user",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "organization",
        "user",
    )
)


def serialize_json(value: GithubRepoOwnerType) -> str:
    return value


def deserialize_json(data: str) -> GithubRepoOwnerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GithubRepoOwnerType value: {data!r}")
    return cast(GithubRepoOwnerType, data)
