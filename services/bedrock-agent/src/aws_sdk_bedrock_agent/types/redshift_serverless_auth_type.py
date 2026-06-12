"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftServerlessAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

RedshiftServerlessAuthType: TypeAlias = Literal[
    "IAM",
    "USERNAME_PASSWORD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "USERNAME_PASSWORD",
    )
)


def serialize_json(value: RedshiftServerlessAuthType) -> str:
    return value


def deserialize_json(data: str) -> RedshiftServerlessAuthType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RedshiftServerlessAuthType value: {data!r}"
        )
    return cast(RedshiftServerlessAuthType, data)
