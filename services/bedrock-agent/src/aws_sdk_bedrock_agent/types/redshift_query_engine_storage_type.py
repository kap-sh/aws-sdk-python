"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

RedshiftQueryEngineStorageType: TypeAlias = Literal[
    "REDSHIFT",
    "AWS_DATA_CATALOG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REDSHIFT",
        "AWS_DATA_CATALOG",
    )
)


def serialize_json(value: RedshiftQueryEngineStorageType) -> str:
    return value


def deserialize_json(data: str) -> RedshiftQueryEngineStorageType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RedshiftQueryEngineStorageType value: {data!r}"
        )
    return cast(RedshiftQueryEngineStorageType, data)
