"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#QueryTransformationMode``."""

from typing import Literal, TypeAlias, cast

QueryTransformationMode: TypeAlias = Literal["TEXT_TO_SQL",]


# --- restJson1 ser/de ---
def serialize_json(value: QueryTransformationMode) -> str:
    return value


def deserialize_json(data: str) -> QueryTransformationMode:
    return cast(QueryTransformationMode, data)
