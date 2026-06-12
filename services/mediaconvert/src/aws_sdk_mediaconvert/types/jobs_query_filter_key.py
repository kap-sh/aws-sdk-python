"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobsQueryFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify job details to filter for while performing a jobs query. You specify these filters as part of a key-value pair within the JobsQueryFilter array. The following list describes which keys are available and their possible values: * queue - Your Queue's name or ARN. * status - Your job's status. (SUBMITTED | PROGRESSING | COMPLETE | CANCELED | ERROR) * fileInput - Your input file URL, or partial input file name. * jobEngineVersionRequested - The Job engine version that you requested for your job. Valid versions are in a YYYY-MM-DD format. * jobEngineVersionUsed - The Job engine version that your job used. This may differ from the version that you requested. Valid versions are in a YYYY-MM-DD format. * audioCodec - Your output's audio codec. (AAC | MP2 | MP3 | WAV | AIFF | AC3| EAC3 | EAC3_ATMOS | VORBIS | OPUS | PASSTHROUGH | FLAC) * videoCodec - Your output's video codec. (AV1 | AVC_INTRA | FRAME_CAPTURE | H_264 | H_265 | MPEG2 | PASSTHROUGH | PRORES | UNCOMPRESSED | VC3 | VP8 | VP9 | XAVC)"""
JobsQueryFilterKey: TypeAlias = Literal[
    "queue",
    "status",
    "fileInput",
    "jobEngineVersionRequested",
    "jobEngineVersionUsed",
    "audioCodec",
    "videoCodec",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "queue",
        "status",
        "fileInput",
        "jobEngineVersionRequested",
        "jobEngineVersionUsed",
        "audioCodec",
        "videoCodec",
    )
)


def serialize_json(value: JobsQueryFilterKey) -> str:
    return value


def deserialize_json(data: str) -> JobsQueryFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobsQueryFilterKey value: {data!r}")
    return cast(JobsQueryFilterKey, data)
