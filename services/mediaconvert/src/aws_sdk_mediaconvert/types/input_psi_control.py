"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputPsiControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Set PSI control for transport stream inputs to specify which data the demux process to scans. * Ignore PSI - Scan all PIDs for audio and video. * Use PSI - Scan only PSI data."""
InputPsiControl: TypeAlias = Literal[
    "IGNORE_PSI",
    "USE_PSI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE_PSI",
        "USE_PSI",
    )
)


def serialize_json(value: InputPsiControl) -> str:
    return value


def deserialize_json(data: str) -> InputPsiControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputPsiControl value: {data!r}")
    return cast(InputPsiControl, data)
