"""Generated from Smithy shape ``com.amazonaws.entityresolution#RecordMatchingModel``."""

from typing import Literal, TypeAlias, cast

RecordMatchingModel: TypeAlias = Literal[
    "ONE_SOURCE_TO_ONE_TARGET",
    "MANY_SOURCE_TO_ONE_TARGET",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordMatchingModel) -> str:
    return value


def deserialize_json(data: str) -> RecordMatchingModel:
    return cast(RecordMatchingModel, data)
