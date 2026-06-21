"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetUseAs``."""

from typing import Literal, TypeAlias, cast

DataSetUseAs: TypeAlias = Literal["RLS_RULES",]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetUseAs) -> str:
    return value


def deserialize_json(data: str) -> DataSetUseAs:
    return cast(DataSetUseAs, data)
