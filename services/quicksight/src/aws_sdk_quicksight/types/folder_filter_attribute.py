"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderFilterAttribute``."""

from typing import Literal, TypeAlias, cast

FolderFilterAttribute: TypeAlias = Literal[
    "PARENT_FOLDER_ARN",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "QUICKSIGHT_OWNER",
    "QUICKSIGHT_VIEWER_OR_OWNER",
    "FOLDER_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> FolderFilterAttribute:
    return cast(FolderFilterAttribute, data)
