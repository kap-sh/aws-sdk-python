"""Generated from Smithy shape ``com.amazonaws.devopsagent#UserType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Types of users in the system</p>"""
UserType: TypeAlias = Literal[
    "IAM",
    "IDC",
    "IDP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "IDC",
        "IDP",
    )
)


def serialize_json(value: UserType) -> str:
    return value


def deserialize_json(data: str) -> UserType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserType value: {data!r}")
    return cast(UserType, data)
