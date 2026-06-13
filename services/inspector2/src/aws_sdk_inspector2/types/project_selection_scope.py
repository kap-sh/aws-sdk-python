"""Generated from Smithy shape ``com.amazonaws.inspector2#ProjectSelectionScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

ProjectSelectionScope: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL",))


def serialize_json(value: ProjectSelectionScope) -> str:
    return value


def deserialize_json(data: str) -> ProjectSelectionScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProjectSelectionScope value: {data!r}")
    return cast(ProjectSelectionScope, data)
