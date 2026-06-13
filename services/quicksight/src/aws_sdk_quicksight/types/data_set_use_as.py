"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetUseAs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DataSetUseAs: TypeAlias = Literal["RLS_RULES",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RLS_RULES",))


def serialize_json(value: DataSetUseAs) -> str:
    return value


def deserialize_json(data: str) -> DataSetUseAs:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSetUseAs value: {data!r}")
    return cast(DataSetUseAs, data)
