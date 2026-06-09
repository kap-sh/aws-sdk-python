"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

ArgoCdRole: TypeAlias = Literal[
    "ADMIN",
    "EDITOR",
    "VIEWER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ADMIN",
        "EDITOR",
        "VIEWER",
    )
)


def serialize_json(value: ArgoCdRole) -> str:
    return value


def deserialize_json(data: str) -> ArgoCdRole:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArgoCdRole value: {data!r}")
    return cast(ArgoCdRole, data)
