"""Generated from Smithy shape ``com.amazonaws.quicksight#CrossDatasetTypes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CrossDatasetTypes: TypeAlias = Literal[
    "ALL_DATASETS",
    "SINGLE_DATASET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_DATASETS",
        "SINGLE_DATASET",
    )
)


def serialize_json(value: CrossDatasetTypes) -> str:
    return value


def deserialize_json(data: str) -> CrossDatasetTypes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CrossDatasetTypes value: {data!r}")
    return cast(CrossDatasetTypes, data)
