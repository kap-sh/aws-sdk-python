"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetFilterAttribute``."""

from typing import Literal, TypeAlias, cast

DataSetFilterAttribute: TypeAlias = Literal[
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DATASET_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> DataSetFilterAttribute:
    return cast(DataSetFilterAttribute, data)
