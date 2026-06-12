"""Generated from Smithy shape ``com.amazonaws.macie2#AdminStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The current status of an account as the delegated Amazon Macie administrator account for an organization in Organizations. Possible values are:</p>"""
AdminStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLING_IN_PROGRESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLING_IN_PROGRESS",
    )
)


def serialize_json(value: AdminStatus) -> str:
    return value


def deserialize_json(data: str) -> AdminStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdminStatus value: {data!r}")
    return cast(AdminStatus, data)
