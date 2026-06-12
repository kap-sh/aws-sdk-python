"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourceSortType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

ResourceSortType: TypeAlias = Literal[
    "DATE",
    "NAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATE",
        "NAME",
    )
)


def serialize_json(value: ResourceSortType) -> str:
    return value


def deserialize_json(data: str) -> ResourceSortType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceSortType value: {data!r}")
    return cast(ResourceSortType, data)
