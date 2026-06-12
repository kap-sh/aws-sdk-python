"""Generated from Smithy shape ``com.amazonaws.finspacedata#ApiAccess``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

ApiAccess: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: ApiAccess) -> str:
    return value


def deserialize_json(data: str) -> ApiAccess:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApiAccess value: {data!r}")
    return cast(ApiAccess, data)
