"""Generated from Smithy shape ``com.amazonaws.quicksight#CrossDatasetTypes``."""

from typing import Literal, TypeAlias, cast

CrossDatasetTypes: TypeAlias = Literal[
    "ALL_DATASETS",
    "SINGLE_DATASET",
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossDatasetTypes) -> str:
    return value


def deserialize_json(data: str) -> CrossDatasetTypes:
    return cast(CrossDatasetTypes, data)
