"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobFilterAttribute``."""

from typing import Literal, TypeAlias, cast

IngestionJobFilterAttribute: TypeAlias = Literal["STATUS",]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> IngestionJobFilterAttribute:
    return cast(IngestionJobFilterAttribute, data)
