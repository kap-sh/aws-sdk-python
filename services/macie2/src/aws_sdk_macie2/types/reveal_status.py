"""Generated from Smithy shape ``com.amazonaws.macie2#RevealStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The status of the configuration for retrieving occurrences of sensitive data reported by findings. Valid values are:</p>"""
RevealStatus: TypeAlias = Literal[
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


def serialize_json(value: RevealStatus) -> str:
    return value


def deserialize_json(data: str) -> RevealStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RevealStatus value: {data!r}")
    return cast(RevealStatus, data)
