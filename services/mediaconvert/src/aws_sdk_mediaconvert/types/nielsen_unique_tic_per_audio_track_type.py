"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NielsenUniqueTicPerAudioTrackType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""To create assets that have the same TIC values in each audio track, keep the default value Share TICs. To create assets that have unique TIC values for each audio track, choose Use unique TICs."""
NielsenUniqueTicPerAudioTrackType: TypeAlias = Literal[
    "RESERVE_UNIQUE_TICS_PER_TRACK",
    "SAME_TICS_PER_TRACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESERVE_UNIQUE_TICS_PER_TRACK",
        "SAME_TICS_PER_TRACK",
    )
)


def serialize_json(value: NielsenUniqueTicPerAudioTrackType) -> str:
    return value


def deserialize_json(data: str) -> NielsenUniqueTicPerAudioTrackType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NielsenUniqueTicPerAudioTrackType value: {data!r}"
        )
    return cast(NielsenUniqueTicPerAudioTrackType, data)
