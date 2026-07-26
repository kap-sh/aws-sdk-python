"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RedshiftQueryEngineType``."""

from typing import Literal, TypeAlias, cast

RedshiftQueryEngineType: TypeAlias = Literal[
    "SERVERLESS",
    "PROVISIONED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftQueryEngineType) -> str:
    return value


def deserialize_json(data: str) -> RedshiftQueryEngineType:
    return cast(RedshiftQueryEngineType, data)
