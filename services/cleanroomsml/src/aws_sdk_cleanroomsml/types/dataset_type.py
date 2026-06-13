"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DatasetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

DatasetType: TypeAlias = Literal["INTERACTIONS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INTERACTIONS",))


def serialize_json(value: DatasetType) -> str:
    return value


def deserialize_json(data: str) -> DatasetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetType value: {data!r}")
    return cast(DatasetType, data)
