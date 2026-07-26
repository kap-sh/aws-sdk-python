"""Generated from Smithy shape ``com.amazonaws.bedrockagent#QueryEngineType``."""

from typing import Literal, TypeAlias, cast

QueryEngineType: TypeAlias = Literal["REDSHIFT",]


# --- restJson1 ser/de ---
def serialize_json(value: QueryEngineType) -> str:
    return value


def deserialize_json(data: str) -> QueryEngineType:
    return cast(QueryEngineType, data)
