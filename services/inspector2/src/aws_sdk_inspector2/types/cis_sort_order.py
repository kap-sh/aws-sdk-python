"""Generated from Smithy shape ``com.amazonaws.inspector2#CisSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

CisSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: CisSortOrder) -> str:
    return value


def deserialize_json(data: str) -> CisSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CisSortOrder value: {data!r}")
    return cast(CisSortOrder, data)
