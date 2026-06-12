"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmfcTimedMetadataBoxVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough."""
CmfcTimedMetadataBoxVersion: TypeAlias = Literal[
    "VERSION_0",
    "VERSION_1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERSION_0",
        "VERSION_1",
    )
)


def serialize_json(value: CmfcTimedMetadataBoxVersion) -> str:
    return value


def deserialize_json(data: str) -> CmfcTimedMetadataBoxVersion:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CmfcTimedMetadataBoxVersion value: {data!r}"
        )
    return cast(CmfcTimedMetadataBoxVersion, data)
