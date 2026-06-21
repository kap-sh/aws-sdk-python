"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MpdTimedMetadataBoxVersion``."""

from typing import Literal, TypeAlias, cast

"""Specify the event message box (eMSG) version for ID3 timed metadata in your output. For more information, see ISO/IEC 23009-1:2022 section 5.10.3.3.3 Syntax. Leave blank to use the default value Version 0. When you specify Version 1, you must also set ID3 metadata to Passthrough."""
MpdTimedMetadataBoxVersion: TypeAlias = Literal[
    "VERSION_0",
    "VERSION_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: MpdTimedMetadataBoxVersion) -> str:
    return value


def deserialize_json(data: str) -> MpdTimedMetadataBoxVersion:
    return cast(MpdTimedMetadataBoxVersion, data)
