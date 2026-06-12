"""Generated from Smithy shape ``com.amazonaws.workdocs#PrincipalRoleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

PrincipalRoleType: TypeAlias = Literal[
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


def serialize_json(value: PrincipalRoleType) -> str:
    return value


def deserialize_json(data: str) -> PrincipalRoleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrincipalRoleType value: {data!r}")
    return cast(PrincipalRoleType, data)
