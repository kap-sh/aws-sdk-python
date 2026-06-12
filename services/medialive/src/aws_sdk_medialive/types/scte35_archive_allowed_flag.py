"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35ArchiveAllowedFlag``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Corresponds to the archive_allowed parameter. A value of ARCHIVE_NOT_ALLOWED corresponds to 0 (false) in the SCTE-35 specification. If you include one of the \"restriction\" flags then you must include all four of them."""
Scte35ArchiveAllowedFlag: TypeAlias = Literal[
    "ARCHIVE_NOT_ALLOWED",
    "ARCHIVE_ALLOWED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARCHIVE_NOT_ALLOWED",
        "ARCHIVE_ALLOWED",
    )
)


def serialize_json(value: Scte35ArchiveAllowedFlag) -> str:
    return value


def deserialize_json(data: str) -> Scte35ArchiveAllowedFlag:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scte35ArchiveAllowedFlag value: {data!r}")
    return cast(Scte35ArchiveAllowedFlag, data)
