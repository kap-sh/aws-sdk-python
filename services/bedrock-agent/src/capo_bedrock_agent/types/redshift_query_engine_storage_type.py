"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineStorageType``."""

from typing import Literal, TypeAlias, cast

RedshiftQueryEngineStorageType: TypeAlias = Literal[
    "REDSHIFT",
    "AWS_DATA_CATALOG",
]


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftQueryEngineStorageType) -> str:
    return value


def deserialize_json(data: str) -> RedshiftQueryEngineStorageType:
    return cast(RedshiftQueryEngineStorageType, data)
