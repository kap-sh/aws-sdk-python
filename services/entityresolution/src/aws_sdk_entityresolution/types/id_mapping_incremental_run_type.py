"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingIncrementalRunType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

IdMappingIncrementalRunType: TypeAlias = Literal["ON_DEMAND",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ON_DEMAND",))


def serialize_json(value: IdMappingIncrementalRunType) -> str:
    return value


def deserialize_json(data: str) -> IdMappingIncrementalRunType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IdMappingIncrementalRunType value: {data!r}"
        )
    return cast(IdMappingIncrementalRunType, data)
