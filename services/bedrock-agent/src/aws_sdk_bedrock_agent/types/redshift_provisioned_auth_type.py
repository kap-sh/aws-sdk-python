"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftProvisionedAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

RedshiftProvisionedAuthType: TypeAlias = Literal[
    "IAM",
    "USERNAME_PASSWORD",
    "USERNAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM",
        "USERNAME_PASSWORD",
        "USERNAME",
    )
)


def serialize_json(value: RedshiftProvisionedAuthType) -> str:
    return value


def deserialize_json(data: str) -> RedshiftProvisionedAuthType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RedshiftProvisionedAuthType value: {data!r}"
        )
    return cast(RedshiftProvisionedAuthType, data)
