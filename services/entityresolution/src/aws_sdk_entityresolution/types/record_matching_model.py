"""Generated from Smithy shape ``com.amazonaws.entityresolution#RecordMatchingModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

RecordMatchingModel: TypeAlias = Literal[
    "ONE_SOURCE_TO_ONE_TARGET",
    "MANY_SOURCE_TO_ONE_TARGET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_SOURCE_TO_ONE_TARGET",
        "MANY_SOURCE_TO_ONE_TARGET",
    )
)


def serialize_json(value: RecordMatchingModel) -> str:
    return value


def deserialize_json(data: str) -> RecordMatchingModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecordMatchingModel value: {data!r}")
    return cast(RecordMatchingModel, data)
