"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSourceFormat``."""

from typing import Literal, TypeAlias, cast

DatasetSourceFormat: TypeAlias = Literal["KNOWLEDGE_BASE",]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSourceFormat) -> str:
    return value


def deserialize_json(data: str) -> DatasetSourceFormat:
    return cast(DatasetSourceFormat, data)
