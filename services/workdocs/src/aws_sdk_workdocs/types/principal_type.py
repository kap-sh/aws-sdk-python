"""Generated from Smithy shape ``com.amazonaws.workdocs#PrincipalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

PrincipalType: TypeAlias = Literal[
    "USER",
    "GROUP",
    "INVITE",
    "ANONYMOUS",
    "ORGANIZATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "GROUP",
        "INVITE",
        "ANONYMOUS",
        "ORGANIZATION",
    )
)


def serialize_json(value: PrincipalType) -> str:
    return value


def deserialize_json(data: str) -> PrincipalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrincipalType value: {data!r}")
    return cast(PrincipalType, data)
