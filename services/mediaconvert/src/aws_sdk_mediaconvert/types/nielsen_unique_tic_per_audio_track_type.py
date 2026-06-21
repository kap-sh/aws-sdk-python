"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NielsenUniqueTicPerAudioTrackType``."""

from typing import Literal, TypeAlias, cast

"""To create assets that have the same TIC values in each audio track, keep the default value Share TICs. To create assets that have unique TIC values for each audio track, choose Use unique TICs."""
NielsenUniqueTicPerAudioTrackType: TypeAlias = Literal[
    "RESERVE_UNIQUE_TICS_PER_TRACK",
    "SAME_TICS_PER_TRACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: NielsenUniqueTicPerAudioTrackType) -> str:
    return value


def deserialize_json(data: str) -> NielsenUniqueTicPerAudioTrackType:
    return cast(NielsenUniqueTicPerAudioTrackType, data)
