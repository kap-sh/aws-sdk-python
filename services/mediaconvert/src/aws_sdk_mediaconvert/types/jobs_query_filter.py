"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobsQueryFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__list_of__string_max100
    import aws_sdk_mediaconvert.types.jobs_query_filter_key


class JobsQueryFilter(TypedDict):
    key: NotRequired[
        "aws_sdk_mediaconvert.types.jobs_query_filter_key.JobsQueryFilterKey"
    ]
    """Specify job details to filter for while performing a jobs query. You specify these filters as part of a key-value pair within the JobsQueryFilter array. The following list describes which keys are available and their possible values: * queue - Your Queue's name or ARN. * status - Your job's status. (SUBMITTED | PROGRESSING | COMPLETE | CANCELED | ERROR) * fileInput - Your input file URL, or partial input file name. * jobEngineVersionRequested - The Job engine version that you requested for your job. Valid versions are in a YYYY-MM-DD format. * jobEngineVersionUsed - The Job engine version that your job used. This may differ from the version that you requested. Valid versions are in a YYYY-MM-DD format. * audioCodec - Your output's audio codec. (AAC | MP2 | MP3 | WAV | AIFF | AC3| EAC3 | EAC3_ATMOS | VORBIS | OPUS | PASSTHROUGH | FLAC) * videoCodec - Your output's video codec. (AV1 | AVC_INTRA | FRAME_CAPTURE | H_264 | H_265 | MPEG2 | PASSTHROUGH | PRORES | UNCOMPRESSED | VC3 | VP8 | VP9 | XAVC)"""
    values: NotRequired[
        "aws_sdk_mediaconvert.types.__list_of__string_max100.__listOf__stringMax100"
    ]
    """A list of values associated with a JobsQueryFilterKey."""


# --- restJson1 ser/de ---
def serialize_json(value: JobsQueryFilter) -> dict:
    out: dict = {}
    if "key" in value:
        import aws_sdk_mediaconvert.types.jobs_query_filter_key

        out["key"] = aws_sdk_mediaconvert.types.jobs_query_filter_key.serialize_json(
            value["key"]
        )
    if "values" in value:
        import aws_sdk_mediaconvert.types.__list_of__string_max100

        out["values"] = (
            aws_sdk_mediaconvert.types.__list_of__string_max100.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> JobsQueryFilter:
    out: JobsQueryFilter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_mediaconvert.types.jobs_query_filter_key

        out["key"] = aws_sdk_mediaconvert.types.jobs_query_filter_key.deserialize_json(
            data["key"]
        )
    if "values" in data:
        import aws_sdk_mediaconvert.types.__list_of__string_max100

        out["values"] = (
            aws_sdk_mediaconvert.types.__list_of__string_max100.deserialize_json(
                data["values"]
            )
        )
    return out
