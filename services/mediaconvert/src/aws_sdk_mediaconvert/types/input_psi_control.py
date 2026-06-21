"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputPsiControl``."""

from typing import Literal, TypeAlias, cast

"""Set PSI control for transport stream inputs to specify which data the demux process to scans. * Ignore PSI - Scan all PIDs for audio and video. * Use PSI - Scan only PSI data."""
InputPsiControl: TypeAlias = Literal[
    "IGNORE_PSI",
    "USE_PSI",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputPsiControl) -> str:
    return value


def deserialize_json(data: str) -> InputPsiControl:
    return cast(InputPsiControl, data)
