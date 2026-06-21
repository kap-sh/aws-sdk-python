"""Generated from Smithy shape ``com.amazonaws.bedrock#QueryTransformationType``."""

from typing import Literal, TypeAlias, cast

QueryTransformationType: TypeAlias = Literal["QUERY_DECOMPOSITION",]


# --- restJson1 ser/de ---
def serialize_json(value: QueryTransformationType) -> str:
    return value


def deserialize_json(data: str) -> QueryTransformationType:
    return cast(QueryTransformationType, data)
