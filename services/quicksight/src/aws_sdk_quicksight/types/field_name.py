"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FieldName: TypeAlias = Literal[
    "assetName",
    "assetDescription",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "assetName",
        "assetDescription",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
    )
)


def serialize_json(value: FieldName) -> str:
    return value


def deserialize_json(data: str) -> FieldName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FieldName value: {data!r}")
    return cast(FieldName, data)
