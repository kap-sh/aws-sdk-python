"""Generated from Smithy shape ``com.amazonaws.workdocs#RoleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

RoleType: TypeAlias = Literal[
    "VIEWER",
    "CONTRIBUTOR",
    "OWNER",
    "COOWNER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VIEWER",
        "CONTRIBUTOR",
        "OWNER",
        "COOWNER",
    )
)


def serialize_json(value: RoleType) -> str:
    return value


def deserialize_json(data: str) -> RoleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoleType value: {data!r}")
    return cast(RoleType, data)
