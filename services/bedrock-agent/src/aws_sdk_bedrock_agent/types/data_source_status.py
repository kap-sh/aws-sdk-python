"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

DataSourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETING",
    "DELETE_UNSUCCESSFUL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "DELETING",
        "DELETE_UNSUCCESSFUL",
    )
)


def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceStatus value: {data!r}")
    return cast(DataSourceStatus, data)
