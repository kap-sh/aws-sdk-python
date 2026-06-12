"""Generated from Smithy shape ``com.amazonaws.greengrassv2#InstalledComponentTopologyFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

InstalledComponentTopologyFilter: TypeAlias = Literal[
    "ALL",
    "ROOT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ROOT",
    )
)


def serialize_json(value: InstalledComponentTopologyFilter) -> str:
    return value


def deserialize_json(data: str) -> InstalledComponentTopologyFilter:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstalledComponentTopologyFilter value: {data!r}"
        )
    return cast(InstalledComponentTopologyFilter, data)
