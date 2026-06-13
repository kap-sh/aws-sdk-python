"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceFilterAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSourceFilterAttribute: TypeAlias = Literal[
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "DATASOURCE_NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "DATASOURCE_NAME",
    )
)


def serialize_json(value: DataSourceFilterAttribute) -> str:
    return value


def deserialize_json(data: str) -> DataSourceFilterAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSourceFilterAttribute value: {data!r}")
    return cast(DataSourceFilterAttribute, data)
