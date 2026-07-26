"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSourceType``."""

from typing import Literal, TypeAlias, cast

DatasetSourceType: TypeAlias = Literal["KENDRA",]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSourceType) -> str:
    return value


def deserialize_json(data: str) -> DatasetSourceType:
    return cast(DatasetSourceType, data)
