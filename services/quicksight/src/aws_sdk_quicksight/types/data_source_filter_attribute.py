"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceFilterAttribute``."""

from typing import Literal, TypeAlias, cast

DataSourceFilterAttribute: TypeAlias = Literal[
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DATASOURCE_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> DataSourceFilterAttribute:
    return cast(DataSourceFilterAttribute, data)
