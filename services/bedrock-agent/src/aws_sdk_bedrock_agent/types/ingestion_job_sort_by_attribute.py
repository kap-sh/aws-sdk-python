"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobSortByAttribute``."""

from typing import Literal, TypeAlias, cast

IngestionJobSortByAttribute: TypeAlias = Literal[
    "STATUS",
    "STARTED_AT",
]


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobSortByAttribute) -> str:
    return value


def deserialize_json(data: str) -> IngestionJobSortByAttribute:
    return cast(IngestionJobSortByAttribute, data)
