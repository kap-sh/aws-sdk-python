"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourceCollectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

ResourceCollectionType: TypeAlias = Literal["SHARED_WITH_ME",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SHARED_WITH_ME",))


def serialize_json(value: ResourceCollectionType) -> str:
    return value


def deserialize_json(data: str) -> ResourceCollectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceCollectionType value: {data!r}")
    return cast(ResourceCollectionType, data)
