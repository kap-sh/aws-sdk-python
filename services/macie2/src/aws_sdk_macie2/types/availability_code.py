"""Generated from Smithy shape ``com.amazonaws.macie2#AvailabilityCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>Specifies whether occurrences of sensitive data can be retrieved for a finding. Possible values are:</p>"""
AvailabilityCode: TypeAlias = Literal[
    "AVAILABLE",
    "UNAVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "UNAVAILABLE",
    )
)


def serialize_json(value: AvailabilityCode) -> str:
    return value


def deserialize_json(data: str) -> AvailabilityCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AvailabilityCode value: {data!r}")
    return cast(AvailabilityCode, data)
