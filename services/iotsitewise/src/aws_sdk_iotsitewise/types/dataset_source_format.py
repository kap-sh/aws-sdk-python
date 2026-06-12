"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSourceFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

DatasetSourceFormat: TypeAlias = Literal["KNOWLEDGE_BASE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KNOWLEDGE_BASE",))


def serialize_json(value: DatasetSourceFormat) -> str:
    return value


def deserialize_json(data: str) -> DatasetSourceFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetSourceFormat value: {data!r}")
    return cast(DatasetSourceFormat, data)
