"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobFilterOperator``."""

from typing import Literal, TypeAlias, cast

IngestionJobFilterOperator: TypeAlias = Literal["EQ",]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> IngestionJobFilterOperator:
    return cast(IngestionJobFilterOperator, data)
