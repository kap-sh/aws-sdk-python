"""Generated from Smithy shape ``com.amazonaws.macie2#MacieStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The status of an Amazon Macie account. Valid values are:</p>"""
MacieStatus: TypeAlias = Literal[
    "PAUSED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PAUSED",
        "ENABLED",
    )
)


def serialize_json(value: MacieStatus) -> str:
    return value


def deserialize_json(data: str) -> MacieStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MacieStatus value: {data!r}")
    return cast(MacieStatus, data)
