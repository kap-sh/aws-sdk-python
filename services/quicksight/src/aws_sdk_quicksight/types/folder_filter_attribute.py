"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "PARENT_FOLDER_ARN",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "QUICKSIGHT_OWNER",
        "QUICKSIGHT_VIEWER_OR_OWNER",
        "FOLDER_NAME",
    )
)


def serialize_json(value: FolderFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> FolderFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FolderFilterAttribute value: {data!r}")
    return cast(FolderFilterAttribute, data)
