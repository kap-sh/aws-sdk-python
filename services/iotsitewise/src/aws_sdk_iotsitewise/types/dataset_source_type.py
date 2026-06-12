"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

DatasetSourceType: TypeAlias = Literal["KENDRA",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KENDRA",))


def serialize_json(value: DatasetSourceType) -> str:
    return value


def deserialize_json(data: str) -> DatasetSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetSourceType value: {data!r}")
    return cast(DatasetSourceType, data)
